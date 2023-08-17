# Importation of packages
from typing import Union, List
from fastapi import FastAPI

# API instanciation
app = FastAPI()


# endpoint : root 
@app.get("/") # How
def read_root(): # What will happen
    return {"Hello": "World"} # Json-like # Simple python types


# endpoint : tuto 
@app.get("/tuto/") # How
def tutorial_processing(op:str, number1 , number2): # What will happen
    "Here is the function of the tutorial"
    operators = {
        "add": None,
        "div": None,
        "mul": None,
    }
    
    return {"Hello": "World"} # Json-like # Simple python types


# endpoint : tuto 
@app.post("/tuto/") # How
def tutorial_processing(op:str, number1 , number2): # What will happen
    "Here is the function of the tutorial"
    operators = {
        "add": number1+number2,
        "div": None,
        "mul": None,
    }
    
    return {"Msg": "Thank you",
            "op":op,
            "result": operators[op] } # Json-like # Simple python types


# endpoint : coutry details
@app.get("/country")
def country(name, code=None):
    """Here is the function that returns the info
    about the selected country"""
    return {}

# endpoint : items
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# enpoint : 
# @app.

# SimpleImpute( missing_values="n/a" )

# class SimpleImpute:
#     def __init__(self, missing_values: Union[str, List[str]] ) -> None:
#         pass

# SimpleImpute( missing_values=["n/a","?", "."] )
