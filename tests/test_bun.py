import pytest
from praktikum.bun import Bun


class TestBun:

    def test_bun_creation(self):
        bun = Bun("Краторная булка", 200)
        assert bun.get_name() == "Краторная булка"
        assert bun.get_price() == 200

    def test_bun_name(self):
        bun = Bun("Флюоресцентная булка", 150)
        assert bun.name == "Флюоресцентная булка"
        assert bun.get_name() == "Флюоресцентная булка"

    def test_bun_price(self):
        bun = Bun("Булка", 99.99)
        assert bun.price == 99.99
        assert bun.get_price() == 99.99