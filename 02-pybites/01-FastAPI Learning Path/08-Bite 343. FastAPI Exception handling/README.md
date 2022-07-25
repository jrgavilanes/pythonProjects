# Subject

https://codechalleng.es/bites/343/

- We only have you add error checking to the create (POST) food entry action / endpoint. The other endpoints are hidden
  in this Bite.

- We only have you use FastAPI's HTTPException with status code 400.

We already handled the food entry not found scenario when updating / deleting in previous Bites using status code 404.

Note that FastAPI also handles using the wrong HTTP verb / method (405) and incomplete (Pydantic) payload issues (422)
for you, nice!

Here are the two use cases we want you to implement:

1. If you call POST with an existing entry.id it effectively overwrites the entry in the food_log dictionary.

In this case, return a 400 response warning the user they should use a PUT (update) request instead with this message:
Food entry already logged, use an update request

2. For this exercise we added a max_daily_calories attribute to the User model.

If you try to add foods beyond this limit (aka "overeat") the API doesn't let you. Return a 400 with this message:
Cannot add more food than daily caloric allowance = {user.max_daily_calories} kcal / day. For this scenario you can
assume all foods are added / evaluated the same day to not overcomplicate things.

Maybe this second scenario should not be the API's responsability, but the point is that you as the developer can impose
limits to your API. Another well known and real world scenario of this is rate limiting to keep your API from being used
incorrectly or unrealisticaly.

Good luck and in the next Bite we'll render some logged foods in an HTML template.