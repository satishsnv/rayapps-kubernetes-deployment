FROM rayproject/ray:2.40.0-py312

# Set the working directory
WORKDIR /mlapps

# Copy your application code into the container
COPY apps/ /mlapps/