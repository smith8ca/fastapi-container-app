"""
This file contains the main FastAPI application.

Functions:
- read_root: Returns a dictionary with a greeting message.
- read_item: Returns a dictionary with the provided item ID and an optional query parameter.
"""

from typing import Union

from fastapi import FastAPI

app = FastAPI(ssl_keyfile="ssl/key.pem", ssl_certfile="ssl/cert.pem")


@app.get("/")
def read_root():
    """
    Returns a dictionary with a single key-value pair.

    Returns:
        dict: A dictionary with the key "Hello" and the value "World".
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Read an item with the given item_id and optional query parameter.

    Parameters:
        item_id (int): The ID of the item to be read.
        q (Union[str, None], optional): The query parameter. Defaults to None.

    Returns:
        dict: A dictionary containing the item_id and q values.
    """
    return {"item_id": item_id, "q": q}
