import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ing_type,name,price,test_description", [
        # Соусы
        (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15, "Стандартный соус"),
        (INGREDIENT_TYPE_SAUCE, "Сыр с астероидной плесенью", 250, "Дорогой соус"),
        (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90, "Острый соус"),

        # Начинки
        (INGREDIENT_TYPE_FILLING, "Говяжий метеорит", 3000, "Дорогая начинка"),
        (INGREDIENT_TYPE_FILLING, "Котлета", 100, "Стандартная начинка"),
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337, "Экзотическая начинка"),

        # Граничные случаи
        ("UNKNOWN_TYPE", "Неизвестный ингредиент", 0, "Неизвестный тип ингредиента"),
        (INGREDIENT_TYPE_SAUCE, "", 50, "Соус с пустым именем"),
        (INGREDIENT_TYPE_FILLING, "Начинка", -10, "Начинка с отрицательной ценой"),
        ("", "", 0, "Полностью пустые значения"),
    ])
    def test_ingredient_creation_and_methods(self, ing_type, name, price, test_description):
        """Параметризованный тест создания ингредиентов и проверки методов"""
        # Создание ингредиента
        ingredient = Ingredient(ing_type, name, price)

        # Проверка методов
        assert ingredient.get_type() == ing_type, f"Ошибка в get_type() для: {test_description}"
        assert ingredient.get_name() == name, f"Ошибка в get_name() для: {test_description}"
        assert ingredient.get_price() == price, f"Ошибка в get_price() для: {test_description}"

        # Проверка прямого доступа к атрибутам (если нужно)
        assert ingredient.type == ing_type, f"Ошибка в атрибуте type для: {test_description}"
        assert ingredient.name == name, f"Ошибка в атрибуте name для: {test_description}"
        assert ingredient.price == price, f"Ошибка в атрибуте price для: {test_description}"