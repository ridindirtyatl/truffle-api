FROM python:3.6.0-slim

RUN pip install flask

COPY . /app

ENV FLASK_APP=/app/app.py \
    PORT=5000

CMD ["python","/app/app.py"]

EXPOSE 5000
