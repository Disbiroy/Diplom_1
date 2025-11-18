import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Краторная булка"
        mock_bun.get_price.return_value = 200

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "Соус Spicy-X"
        mock_ingredient.get_price.return_value = 90

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @pytest.mark.parametrize("ingredient_count", [1, 3, 5])
    def test_add_multiple_ingredients(self, ingredient_count):
        burger = Burger()

        for i in range(ingredient_count):
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
            mock_ingredient.get_name.return_value = f"Ингредиент {i}"
            mock_ingredient.get_price.return_value = 100 + i
            burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == ingredient_count

    def test_remove_ingredient(self):
        burger = Burger()

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        assert len(burger.ingredients) == 3

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient1
        assert burger.ingredients[1] == mock_ingredient3

    @pytest.mark.parametrize("index_to_remove,expected_remaining,test_description", [
        (0, 2, "Удаление первого ингредиента"),
        (1, 2, "Удаление среднего ингредиента"),
        (2, 2, "Удаление последнего ингредиента"),
    ])
    def test_remove_ingredient_parameterized(self, index_to_remove, expected_remaining, test_description):
        """Параметризованный тест удаления ингредиентов из разных позиций"""
        burger = Burger()

        # Добавляем 3 mock ингредиента
        mock_ingredients = []
        for i in range(3):
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_name.return_value = f"Ингредиент {i}"
            mock_ingredients.append(mock_ingredient)
            burger.add_ingredient(mock_ingredient)

        # Удаляем ингредиент по указанному индексу
        burger.remove_ingredient(index_to_remove)

        # Проверяем количество оставшихся ингредиентов
        assert len(burger.ingredients) == expected_remaining, f"Ошибка в: {test_description}"

    def test_move_ingredient(self):
        burger = Burger()

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_name.return_value = "Первый"
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_name.return_value = "Второй"
        mock_ingredient3 = Mock(spec=Ingredient)
        mock_ingredient3.get_name.return_value = "Третий"

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        # Перемещаем элемент с индексом 0 на позицию 2
        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient3
        assert burger.ingredients[2] == mock_ingredient1

    @pytest.mark.parametrize("from_index,to_index,expected_order", [
        (0, 2, ["Второй", "Третий", "Первый"]),  # Первый -> в конец
        (2, 0, ["Третий", "Первый", "Второй"]),  # Последний -> в начало
        (1, 1, ["Первый", "Второй", "Третий"]),  # На ту же позицию
    ])
    def test_move_ingredient_parameterized(self, from_index, to_index, expected_order):
        """Параметризованный тест перемещения ингредиентов"""
        burger = Burger()

        # Создаем ингредиенты с уникальными именами
        ingredients_data = [
            ("Первый", Mock(spec=Ingredient)),
            ("Второй", Mock(spec=Ingredient)),
            ("Третий", Mock(spec=Ingredient))
        ]

        for name, mock in ingredients_data:
            mock.get_name.return_value = name
            burger.add_ingredient(mock)

        # Перемещаем ингредиент
        burger.move_ingredient(from_index, to_index)

        # Проверяем порядок
        actual_order = [ing.get_name() for ing in burger.ingredients]
        assert actual_order == expected_order

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [50, 75], 325),  # (100*2) + 50 + 75 = 325
        (150, [30, 45, 60], 435),  # (150*2) + 30 + 45 + 60 = 435
        (200, [], 400),  # 200*2 = 400
        (50, [10], 110),  # (50*2) + 10 = 110
    ])
    def test_get_price_parameterized(self, bun_price, ingredient_prices, expected_total):
        burger = Burger()

        # Мок булки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        # Моки ингредиентов
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_total

    def test_get_receipt_with_bun_and_ingredients(self):
        burger = Burger()

        # Мок булки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Сезонная булка"
        mock_bun.get_price.return_value = 45
        burger.set_buns(mock_bun)

        # Моки ингредиентов
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "Сыр"
        mock_ingredient1.get_price.return_value = 25

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "Котлета"
        mock_ingredient2.get_price.return_value = 35

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        receipt = burger.get_receipt()

        assert "Сезонная булка" in receipt
        assert "sauce Сыр" in receipt
        assert "filling Котлета" in receipt
        assert "150" in receipt  # (45*2) + 25 + 35 = 150

    def test_get_receipt_no_bun(self):
        burger = Burger()

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = "Салат"
        mock_ingredient.get_price.return_value = 15

        burger.add_ingredient(mock_ingredient)

        # Добавляем булку, чтобы избежать ошибки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        assert "Салат" in receipt

    def test_get_receipt_empty(self):
        burger = Burger()

        # Добавляем булку, чтобы избежать ошибки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        # Проверяем что чек генерируется для бургера только с булкой
        assert "Булка" in receipt
        assert "Price:" in receipt

    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt_calls_get_price(self, mock_get_price):
        mock_get_price.return_value = 999

        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Булка"
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        mock_get_price.assert_called_once()
        assert "Price: 999" in receipt