import main


def test_food_model():
    try:
        print()
        food = main.Food(
            id=1,
            name="ajo",
            serving_size=12,
            kcal_per_serving=12,
            protein_grams=56,
            fibre_grams=567
        )
        print(food)

        food = main.Food(
            id=1,
            name="ajo",
            serving_size=12,
            kcal_per_serving=12,
            protein_grams=56
        )
        print(food)
        assert True

    except Exception as e:
        print(e)
        assert False
