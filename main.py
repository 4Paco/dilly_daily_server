from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Change to specific domains if needed.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ingredients")
async def all_ingredients():
    with open('data/ingredients.json') as json_data:
        data = json.load(json_data,) 
    return data

@app.get("/recipes")
async def all_recipes():
    with open('data/recipes.json') as json_data:
        data = json.load(json_data,) 
    return data
#@app.get("/recipes/{recipe_id}")
#async def one_recipe():
#    with open('data/recipes.json') as json_data:
#        data = json.load(json_data,) 
#    return data

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
