FROM python:3.8-slim-buster
WORKDIR /code
RUN pip install pipenv
COPY Pipfile .
RUN pipenv install
COPY src/main.py .
COPY /usr/bin/geckodriver .
CMD ["pipenv", "run", "python", "main.py"]
