from datetime import datetime
from typing import Dict, Any

import uvicorn
from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll export authentication further in a later Bite
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse

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

HTML_TEMPLATE = """<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Food log for {username}</title>
</head>

<body>
    <table>
        <thead>
            <th>Food</th>
            <th>Added</th>
            <th>Servings</th>
            <th>Calories (kcal)</th>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
    </table>

</body>
</html>"""
TABLE_ROW = """<tr>
    <td>{food_name}</td>
    <td>{date_added}</td>
    <td>{number_servings} x {serving_size}</td>
    <td>{total_calories}</td>
</tr>"""


@app.post("/", status_code=201)
async def create_food_entry(entry: FoodEntry):
    """Previous Bite and used in test"""
    food_log[entry.id] = entry
    return entry


@app.get("/{username}", response_class=HTMLResponse)
async def show_foods_for_user(request: Request, username: str):
    # 1. extract foods for user using the food_log dict
    user_food_entries = [f for f in food_log.values() if f.user.username == username]
    # 2. build up the embedded html string
    table_rows = ""
    for entry in user_food_entries:
        aux = TABLE_ROW
        aux = aux.replace("{food_name}", entry.food.name)
        aux = aux.replace("{date_added}", str(entry.date_added))
        aux = aux.replace("{number_servings}", str(entry.number_servings))
        aux = aux.replace("{serving_size}", entry.food.serving_size)
        aux = aux.replace("{total_calories}", str(entry.food.kcal_per_serving * entry.number_servings))
        table_rows += aux
    # 3. return an HTMLResponse (with the html content and status code 200)
    return HTML_TEMPLATE.replace("{username}", username).replace("{table_rows}", table_rows)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# /** solution given **/
# @app.get("/{username}", response_class=HTMLResponse)
# async def show_foods_for_user(request: Request, username: str):
#     user_food_log = [fl for fl in food_log.values() if fl.user.username == username]
#
#     table_rows = "\n".join(
#         [
#             TABLE_ROW.format(
#                 food_name=fl.food.name,
#                 date_added=fl.date_added,
#                 number_servings=fl.number_servings,
#                 serving_size=fl.food.serving_size,
#                 total_calories=fl.total_calories,
#             )
#             for fl in user_food_log
#         ]
#     )
#     html_content = HTML_TEMPLATE.format(username=username, table_rows=table_rows)
#
#     return HTMLResponse(content=html_content, status_code=200)
