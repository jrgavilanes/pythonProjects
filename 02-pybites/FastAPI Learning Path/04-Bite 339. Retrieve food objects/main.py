from typing import Dict, List
import uvicorn
from fastapi import FastAPI
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
    """Endpoint from Bite 03"""
    foods[food.id] = food
    # print(foods)
    return food


@app.get("/", response_model=List[Food])
def read_foods():
    # print(foods)
    # result = []
    # for f in foods:
    #     result.append(foods[f])
    # return result
    return [foods[i] for i in foods]
    # return list(foods.values())


@app.get("/{id_food}", response_model=Food)
def read_food(id_food: int):
    # print(foods[id_food])
    return foods[id_food]


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)


# ***** SOLUCIÓN DADA *******

# from typing import Dict, List
#
# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# class Food(BaseModel):
#     """Model from Bite 02"""
#
#     id: int
#     name: str
#     serving_size: str
#     kcal_per_serving: int
#     protein_grams: float
#     fibre_grams: float = 0
#
#
# app = FastAPI()
# foods: Dict[int, Food] = {}
#
#
# @app.post("/", status_code=201)
# async def create_food(food: Food):
#     """Endpoint from Bite 03"""
#     foods[food.id] = food
#     return food
#
#
# @app.get("/", response_model=List[Food])
# async def read_foods():
#     return list(foods.values())
#
#
# @app.get("/{food_id}", response_model=Food)
# async def read_food(food_id: int):
#     return foods[food_id]