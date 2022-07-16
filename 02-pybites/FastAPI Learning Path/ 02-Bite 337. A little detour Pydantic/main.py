from pydantic import BaseModel


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


def main():
    try:
        food = Food(
            id=1,
            name="ajo",
            serving_size=12,
            kcal_per_serving=12,
            protein_grams=56,
            fibre_grams=567
        )
        print(food)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
