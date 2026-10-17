import pytest
from unittest.mock import Mock
from burger import Burger

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "bun"
    bun.get_price.return_value = 200.0
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_type.return_value = "sauce"
    ingredient.get_name.return_value = "spicy-X"
    ingredient.get_price.return_value = 80.0
    return ingredient

@pytest.fixture
def full_burger(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger