"""
main.py

A sample FastAPI application.
"""

from typing import Union
from fastapi import FastAPI


app = FastAPI(ssl_keyfile="ssl/key.pem", ssl_certfile="ssl/cert.pem")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
