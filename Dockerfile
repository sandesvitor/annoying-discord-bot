FROM ubuntu:latest
WORKDIR /app
RUN apt update && \
    apt install python3-pip -y
RUN pip install pipenv
COPY . .
RUN pipenv install
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -y && apt install wget firefox -y && \
    wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xzvf geckodriver* && \
    chmod +x geckodriver && \
    mv geckodriver /usr/local/bin/
    
CMD ["pipenv", "run", "python", "src/main.py"]
