from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.five_btn=(By.CSS_SELECTOR, "[jsname='Ax5wH']")
        self.plus_btn=(By.CSS_SELECTOR, "[jsname='XSr6wc']")
        self.one_btn=(By.CSS_SELECTOR, "[jsname='N10B9']")
        self.zero_btn=(By.CSS_SELECTOR, "[jsname='bkEvMb']")
        self.equal_btn=(By.CSS_SELECTOR, "[jsname='Pt8tGc']")
        self.result_btn=(By.CSS_SELECTOR, "[jsname='VssY5c']")
        self.buttons=(By.CSS_SELECTOR, "div.SKWP2e table tr div div")


    def check_btn_element(self, btn):
        return "\n" not in btn.text and btn.text != ""
    def get_btns_count(self, condition= None):
        btns=self.get_elements(self.buttons)
        btn_count=0
        for btn in btns:
            btn_text=btn.text
            if self.check_btn_element(btn):
                if condition is not None:
                    if btn_text.isnumeric():
                        btn_count += 1
                else:
                    btn_count += 1
        return btn_count


    def get_result(self):
        return self.get_text(self.result_btn)
    def click_equal_btn(self):
        self.click(self.equal_btn)
    def click_five_btn(self):
        self.click(self.five_btn)

    def click_plus_btn(self):
        self.click(self.plus_btn)

    def click_one_btn(self):
        self.click(self.one_btn)

    def click_zero_btn(self):
        self.click(self.zero_btn)