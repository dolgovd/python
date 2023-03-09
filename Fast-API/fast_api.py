# Description (TBD)
# Libraries: fastapi, uvicorn
# Run uvicorn: uvicorn fast_api:app --reload
#              http://127.0.0.1:8000/docs

from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    brandprice: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

# @app.get("/")
# def home():
#     return {"Data": "Test"}

# @app.get("/about")
# def about():
#     return {"Data": "About"}

inventory = {
    1: {
        "name": "bycicle",
        "price": 3000,
        "brand": "TREK"
    }
}

# Path / Endpoint parameters
# 127.0.0.1:8000/get-item/1
@app.get("/get-item/{item_id}")
def get_item(item_id: int= Path(None, description="Item ID")):
    return inventory[item_id]

# Query parameters
# http://127.0.0.1:8000/get-by-name?name=bycicle
@app.get("/get-by-name")
def get_by_name(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

# Request body & POST method
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    else:
        inventory[item_id] = item
        return inventory[item_id]
    
# PUT method
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist"}

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

# DELETE method
@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="Item ID")):
    if item_id not in inventory:
        return {"Error" : "Item ID does not exist"}
    else:
        del inventory[item_id]