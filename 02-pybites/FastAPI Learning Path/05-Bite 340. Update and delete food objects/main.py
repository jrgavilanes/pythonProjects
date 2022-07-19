from typing import Dict, List
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


@app.post("/", status_code=201)
def create_food(food: Food):
    foods[food.id] = food
    return food


@app.get("/", response_model=List[Food])
def read_foods():
    return list(foods.values())


@app.get("/{id_food}", response_model=Food)
def read_food(id_food: int):
    return foods[id_food]


@app.delete("/{id_food}")
def read_food(id_food: int):
    if id_food not in foods:
        raise HTTPException(status_code=404, detail="Food not found")
    del foods[id_food]
    return {"ok": True}


@app.put("/{id_food}")
def read_food(id_food: int, food: Food):
    if id_food not in foods:
        raise HTTPException(status_code=404, detail="Food not found")
    foods[id_food] = foodl
    return foods[id_food]


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
