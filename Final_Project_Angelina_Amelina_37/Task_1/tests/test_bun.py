import pytest

from bun import Bun
from data import BUNS_DATA

class TestBun:
    @pytest.mark.parametrize("bun_info", BUNS_DATA)
    def test_get_name_return_bun_name(self, bun_info):
        bun = Bun(bun_info["bun_name"], bun_info["bun_price"])

        assert bun.get_name() == bun_info["bun_name"]

    @pytest.mark.parametrize("bun_info", BUNS_DATA)
    def test_get_price_return_price(self, bun_info):
        bun = Bun(bun_info["bun_name"], bun_info["bun_price"])

        assert bun.get_price() == bun_info["bun_price"]