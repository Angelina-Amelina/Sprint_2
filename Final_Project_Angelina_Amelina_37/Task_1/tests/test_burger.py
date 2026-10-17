import pytest
from unittest.mock import Mock
from burger import Burger

class TestBurger:

    def test_constructor_set_none_bun_and_empty_ingredient_list(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns_set_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_add_to_list(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_remove_by_index(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_change_position(self, burger, mock_ingredient):
        second_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [second_ingredient, mock_ingredient]

    def test_get_price_return_correct_price(self, full_burger):
        assert full_burger.get_price() == 480.0

    def test_get_receipt_return_correct_receipt(self, full_burger):
        expected = """(==== bun ====)
= sauce spicy-X =
(==== bun ====)

Price: 480.0"""
        assert full_burger.get_receipt() == expected

   # Проверяем, что при удалении из пустого бургера вызывается ошибка индекса
    def test_remove_ingredient_raises_index_error_for_index(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
   # Проверяем, что при перемещении в пустом бургере вызываетя ошибка индекса
    def test_move_ingredient_raises_index_error_for_empty_list(self, burger):
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)
   # Проверяем, что расчет цены без булки вызовет ошибку
    def test_get_price_raises_attribute_error_without_bun(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()
   # Проверяем, что печать чека без булки вызовет ошибку
    def test_get_receipt_raises_attribute_error_without_bun(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()

