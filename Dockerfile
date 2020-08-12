FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]