FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# CMD ["fastapi", "run", "app/main.py", "--port", "80"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "ssl/key.pem", "--ssl-certfile", "ssl/cert.pem"]
