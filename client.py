import requests

response = requests.post("http://localhost:8200/translate", params={"text": "Hello world!"})
french_text = response.json()


print(french_text)

text = """Paris is the capital and most populous city of France,
    with an estimated population of 2,175,601 residents as of 2018, in an area of more than 105 square kilometres (41 square miles). 
    The City of Paris is the centre and seat of government of the region and province of Île-de-France, or Paris Region, which has an estimated population of 12,174,880, or about 18 percent of the population of France as of 2017."""

response = requests.post("http://localhost:8200/summarize", params={"text": text})
res = response.json()


print(res)