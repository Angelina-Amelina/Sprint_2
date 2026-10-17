import pytest
from ingredient import Ingredient
from data import INGREDIENTS_DATA

class TestIngredient:

    @pytest.mark.parametrize("ingredient_info", INGREDIENTS_DATA)
    def test_get_price_return_correct_price(self, ingredient_info):
        ingredient = Ingredient(ingredient_info["ingredient_type"],
                                ingredient_info["ingredient_name"],
                                ingredient_info["ingredient_price"])
        assert ingredient.get_price() == ingredient_info["ingredient_price"]


    @pytest.mark.parametrize("ingredient_info", INGREDIENTS_DATA)
    def test_get_name_return_correct_name(self, ingredient_info):
        ingredient = Ingredient(ingredient_info["ingredient_type"],
                                ingredient_info["ingredient_name"],
                                ingredient_info["ingredient_price"])
        assert ingredient.get_name() == ingredient_info["ingredient_name"]


    @pytest.mark.parametrize("ingredient_info", INGREDIENTS_DATA)
    def test_get_type_return_correct_type(self, ingredient_info):
        ingredient = Ingredient(ingredient_info["ingredient_type"],
                                ingredient_info["ingredient_name"],
                                ingredient_info["ingredient_price"])
        assert ingredient.get_type() == ingredient_info["ingredient_type"]