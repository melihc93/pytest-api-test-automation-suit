FROM python:3.7

WORKDIR /test_api

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./run.py"]