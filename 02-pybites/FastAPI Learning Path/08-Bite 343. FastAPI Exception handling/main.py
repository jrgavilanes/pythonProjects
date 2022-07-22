import uvicorn
from datetime import datetime
from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll explore further in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

AVG_HUMAN_CALORIES_PER_DAY = 2250


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


class User(BaseModel):
    id: int
    username: str
    password: str
    max_daily_calories: int = AVG_HUMAN_CALORIES_PER_DAY

    def __init__(self, **data: Any):
        data["password"] = get_password_hash(data["password"])
        super().__init__(**data)


class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    @property
    def total_calories(self):
        return self.food.kcal_per_serving * self.number_servings


app = FastAPI()
food_log: Dict[int, FoodEntry] = {}


# To focus on exception handling we only work on Create
# in this Bite hiding read-update-delete endpoints.


@app.post("/", status_code=201)
async def create_food_entry(entry: FoodEntry):
    # TODO: add exception handling code here
    if entry.id in food_log:
        raise HTTPException(status_code=400, detail="Food entry already logged, use an update request")

    entry_calories = entry.food.kcal_per_serving * entry.number_servings

    previous_calories = sum([e.food.kcal_per_serving * e.number_servings
                             for e in food_log.values()
                             if e.user.id == entry.user.id
                             ])
    if (entry_calories + previous_calories) > entry.user.max_daily_calories:
        raise HTTPException(status_code=400,
                            detail=f"Cannot add more food than daily caloric allowance = {entry.user.max_daily_calories} kcal / day")

    food_log[entry.id] = entry
    return entry


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
