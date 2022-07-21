# Subject

https://codechalleng.es/bites/342/

- create_food_entry() [POST] -> receives a FoodEntry, adds it to food_log and returns it.

- get_foods_for_user() [GET] -> receives a user_id, filters food_log and returns the foods logged for that user (List[FoodEntry]).

- update_food_entry() [PUT] -> receives an entry_id and new FoodEntry, updates the corresponding entry and returns the new FoodEntry, raises an HTTPException if the entry is not found.

- delete_food_entry() [DELETE] -> receives an entry_id and deletes it from food_log, raises an HTTPException if the entry is not found.

We'll hide the previous Food CRUD in the template for now to force the deliberate practice!

Because the platform supports single modules only for exercises, we embedded all three Pydantic models so you might need to scroll down a bit.

Again, we use an in-memory dictionary (food_log: Dict[int, Food]) to focus on the FastAPI / Pydantic (typing) part.

In the SQLModel learning path we'll cover databases and ORMs.

At the end of this Bite you'll have a simple API to track foods. Super exciting!

But it's not very robust yet, so in the next Bite we'll add exception handling.

Then we take a detour to some web development, having you show a user's food log in an HTML template.

In the final Bite we'll lock down the API so only logged-in users can track their own foods.