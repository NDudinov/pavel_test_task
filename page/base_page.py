from playwright.sync_api import Page, Response


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url) -> Response:
        return self.page.goto(url)
