FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

ENTRYPOINT ["python", "python_bot/main.py"]
