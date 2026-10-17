from bun import Bun
from ingredient import Ingredient

class TestDatabase:
    def test_available_buns_return_correct_count(self, db):
        assert len(db.available_buns()) == 3

    def test_available_buns_return_correct_type(self, db):
        assert isinstance(db.available_buns()[0], Bun)

    def test_available_ingredients_returns_correct_count(self, db):
        assert len(db.available_ingredients()) == 6

    def test_available_ingredients_return_correct_type(self, db):
        assert isinstance(db.available_ingredients()[0], Ingredient)