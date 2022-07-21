from datetime import datetime
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
import uvicorn
from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll export authentication further in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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


# We've hidden the previous Food CRUD to keep it compact and to force you to
# repeat the API building process (deliberate practice is key!)

# Create CRUD endpoints for FoodEntry below as per instructions in the Bite ...
@app.get("/{user_id}", status_code=200)
def get_foods_for_user(user_id: int):
    return [f
            for f in food_log.values()
            if f.user.id == user_id]


@app.post("/", status_code=201)
def get_foods_for_user(food_entry: FoodEntry):
    food_log[food_entry.id] = food_entry
    return food_entry


@app.put("/{entry_id}")
def update_food_entry(entry_id: int, food_entry: FoodEntry):
    if entry_id not in food_log:
        raise HTTPException(status_code=404, detail="Food entry not found")
    food_log[entry_id] = food_entry
    return food_log[entry_id]


@app.delete("/{entry_id}")
def delete_food_entry(entry_id: int):
    if entry_id not in food_log:
        raise HTTPException(status_code=404, detail="Food entry not found")
    del food_log[entry_id]
    return {"ok": True}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
