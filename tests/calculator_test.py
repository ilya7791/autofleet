from pages.calculator_page import CalculatorPage
from tests.base_test import BaseTest

class TestCalculator(BaseTest):
    def test_calculator(self):

        groups_obj=CalculatorPage(self.driver)
        groups_obj.click_five_btn()
        groups_obj.click_plus_btn()
        groups_obj.click_one_btn()
        groups_obj.click_zero_btn()
        groups_obj.click_equal_btn()
        result=groups_obj.get_result()
        assert result == "15"

        numeric_count=groups_obj.get_btns_count(condition="numeric btns")
        assert numeric_count == 10

        all_btns_count = groups_obj.get_btns_count()
        assert all_btns_count == 35



