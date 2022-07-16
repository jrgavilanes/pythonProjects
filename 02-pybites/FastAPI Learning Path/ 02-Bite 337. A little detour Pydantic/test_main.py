import main


def test_Food_Model():
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

    except:
        assert False
