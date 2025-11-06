import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_initialization(self):
        db = Database()

        # Проверяем, что булки созданы
        buns = db.available_buns()
        assert len(buns) == 3
        assert isinstance(buns[0], Bun)
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

        # Проверяем, что ингредиенты созданы
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()

        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ]

        for i, (expected_name, expected_price) in enumerate(expected_buns):
            assert buns[i].get_name() == expected_name
            assert buns[i].get_price() == expected_price

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        # Проверяем соусы
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100

        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200

        # Проверяем начинки
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100

        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200