# service.py
from fastapi import FastAPI
from ray import serve
import torch
from transformers import BartForConditionalGeneration, BartTokenizer


app = FastAPI()


@serve.deployment()
@serve.ingress(app)
class Summarizer:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        model_name = "facebook/bart-large-cnn"
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name).to(self.device)


    @app.post("/")
    def summarize(self, text: str) -> str:
        max_length = 50
        min_length = 10
        no_repeat_ngram_size = 3
        length_penalty = 2.0
        num_beams = 4

        with torch.no_grad():
            answers_input_ids = self.tokenizer.batch_encode_plus(
                [text], return_tensors="pt", truncation=True, max_length=max_length
            )["input_ids"].to(self.device)
            summary_ids = self.model.generate(
                answers_input_ids,
                num_beams=num_beams,
                length_penalty=length_penalty,
                max_length=max_length,
                min_length=min_length,
                no_repeat_ngram_size=no_repeat_ngram_size,
            )

            exec_sum = self.tokenizer.decode(
                summary_ids.squeeze(), skip_special_tokens=True
            )
        return exec_sum

deployment = Summarizer.bind()