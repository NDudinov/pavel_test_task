import re
from playwright.sync_api import Page, expect

class TestUIAwarasleep:
    def test_ui_awara(self, page: Page) -> None:
        url = 'https://qa.awarasleep.com'
        page.goto(url)
        expect(page).to_have_title(re.compile("Awara"))
        hero_shop = page.locator("//*[@data-testid='hero_shop_mattress']")
        hero_shop.click()
        expect(page).to_have_url(re.compile(f"{url}/mattress"))
        add_to_cart_button = page.locator("//*[@data-testid='addtocart_btn']")
        add_to_cart_button.click()
        cart = page.locator("//*[@data-testid='cart_items_area']", has=page.get_by_text("Awara Latex Hybrid Mattress "))
        expect(cart).to_be_visible()