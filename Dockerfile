FROM python:3.6.0-slim

RUN pip install flask

COPY . /app

ENV FLASK_APP=/app/app.py

ENTRYPOINT ["python", "-m", "flask"]

CMD ["run", "--host=0.0.0.0"]

EXPOSE 5000
