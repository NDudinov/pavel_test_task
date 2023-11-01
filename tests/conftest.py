import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption("--br", action="store", default="chrome")
    parser.addoption("--headless", action="store", type=bool, default=False)


@pytest.fixture(scope="session")
def browser(request):
    print("browser initiated ________________________________________")
    global browser

    browser_name = request.config.getoption("--br")

    play = sync_playwright().start()

    match browser_name:
        case "chrome":
            browser = play.chromium.launch(
                headless=request.config.getoption("--headless")
            )

        case "firefox":
            browser = play.firefox.launch(
                headless=request.config.getoption("--headless")
            )

        case "webkit":
            browser = play.webkit.launch(
                headless=request.config.getoption("--headless")
            )

        case _:
            print(f"{browser_name} browser is not available!")

    yield browser

    print("browser destroyed ________________________________________")
    browser.close()
    play.stop()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
