import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_ingredient_creation_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredient.get_name() == "Соус традиционный галактический"
        assert ingredient.get_price() == 15

    def test_ingredient_creation_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит", 3000)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
        assert ingredient.get_name() == "Говяжий метеорит"
        assert ingredient.get_price() == 3000

    def test_ingredient_attributes(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Сыр с астероидной плесенью", 250)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "Сыр с астероидной плесенью"
        assert ingredient.price == 250