from playwright.sync_api import Page, Locator, expect


class AwaraCheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def check_item_in_cart(self, item_name: str) -> Locator:
        expect(
            self.page.locator(
                "//*[@data-testid='cart_items_area']",
                has=self.page.get_by_text(item_name),
            )
        ).to_be_visible()
