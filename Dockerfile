FROM python:3.6.0-slim

COPY requirements.txt /app/requirements.txt

RUN apt-get update \
 && apt-get install -y build-essential

RUN pip install -r /app/requirements.txt

COPY . /app

ENV PORT=5000

WORKDIR /app

CMD ["python", "app.py"]

EXPOSE 5000
