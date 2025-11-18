import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name,price,test_description", [
        # Основные тест-кейсы
        ("Краторная булка", 200, "Стандартная булка с ценой 200"),
        ("Флюоресцентная булка", 150, "Флюоресцентная булка с ценой 150"),
        ("Булка", 99.99, "Булка с дробной ценой"),

        # Граничные случаи
        ("", 0, "Пустое имя и нулевая цена"),
        ("Тестовая булка", -100, "Отрицательная цена"),
        ("Очень длинное название булки для тестирования", 1000, "Длинное имя булки"),
        ("Булка с спецсимволами !@#$%", 500, "Булка со спецсимволами"),
    ])
    def test_bun_creation_and_methods(self, name, price, test_description):
        """Параметризованный тест создания булок и проверки методов"""
        # Создание булки
        bun = Bun(name, price)

        # Проверка методов get_name() и get_price()
        assert bun.get_name() == name, f"Ошибка в get_name() для: {test_description}"
        assert bun.get_price() == price, f"Ошибка в get_price() для: {test_description}"

        # Проверка прямого доступа к атрибутам (если нужно)
        assert bun.name == name, f"Ошибка в атрибуте name для: {test_description}"
        assert bun.price == price, f"Ошибка в атрибуте price для: {test_description}"