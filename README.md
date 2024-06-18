## Generate SSL Certificates

To create new SSL certificates, run the following from the root directory and provide the necessary information on the command line:

```bash
openssl req -x509 -newkey rsa:4096 -nodes -out ssl/cert.pem -keyout ssl/key.pem -days 365
```

## Run Locally

To run the application locally, execute the following from the root directory:

```bash
uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile ssl/key.pem --ssl-certfile ssl/cert.pem
```

The API application can also be launched with `fastapi`:

```bash
fastapi run main.py --host 0.0.0.0 --port 80
```

## Docker Container Development

Build docker image:

```bash
docker build -t docker-fastapi .
```

Run the docker image:

```bash
docker run -d --name fastapi -p 443:443 docker-fastapi
```

## Sources & References

- [Adding HTTPS to FastAPI](https://medium.com/@mariovanrooij/adding-https-to-fastapi-ad5e0f9e084e)
