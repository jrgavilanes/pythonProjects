from typing import Dict

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


# write the Create endpoint
@app.post("/", status_code=201)
def create_food(food: Food):
    foods[food.id] = food
    print(foods)
    return food


@app.get("/")
def home():
    return {"result": "ok"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
