import re

from playwright.sync_api import Page, expect

from page.awara.awara_matress_page import AwaraMatressPage
from utils import ui_const


class AwaraMainPage:
    def __init__(self, page: Page):
        self.page = page
        self.hero_shop = page.locator("//*[@data-testid='hero_shop_mattress']")

    def open(self) -> None:
        self.page.goto(ui_const.AWARA_URL)

    def check_title(self) -> None:
        expect(self.page).to_have_title(re.compile("Awara"))

    def click_hero_shop(self) -> AwaraMatressPage:
        self.hero_shop.click()
        return AwaraMatressPage(self.page)
