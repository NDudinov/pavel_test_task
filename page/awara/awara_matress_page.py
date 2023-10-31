import re

from playwright.sync_api import Page, expect

from page.awara.awara_checkout_page import AwaraCheckoutPage
from utils import ui_const


class AwaraMatressPage:
    matress_endpoint = "/mattress"

    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart = page.locator("//*[@data-testid='addtocart_btn']")

    def check_url(self) -> None:
        expect(self.page).to_have_url(
            re.compile(f"{ui_const.AWARA_URL}{self.matress_endpoint}")
        )

    def click_add_to_cart(self) -> AwaraCheckoutPage:
        self.add_to_cart.click()
        return AwaraCheckoutPage(self.page)
