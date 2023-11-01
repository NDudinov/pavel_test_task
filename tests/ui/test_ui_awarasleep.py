import allure
import pytest

from page.awara.awara_main_page import AwaraMainPage


@pytest.mark.ui_test
class TestUIAwarasleep:
    @allure.testcase("UI Test")
    def test_ui_awara(self, page) -> None:
        with allure.step(
            "1. Open https://qa.awarasleep.com/ -> check the page is opened"
        ):
            main_page = AwaraMainPage(page)
            main_page.open()
            main_page.check_title()
        with allure.step(
            "2. Click the “Shop & Save” button on the Hero Banner -> check you are on "
            "/mattress"
        ):
            matress_page = main_page.click_hero_shop()
            matress_page.check_url()
        with allure.step(
            "3. Add the mattress to the cart -> Check the mattress has been added to "
            "the cart"
        ):
            checkout_page = matress_page.click_add_to_cart()
            checkout_page.check_item_in_cart("Awara Latex Hybrid Mattress ")
