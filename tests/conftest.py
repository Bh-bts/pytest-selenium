import pytest
from selenium import webdriver
from config.config import TestData

@pytest.fixture(scope="class")
def setUp(request, browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser")
    else:
        raise ValueError(f"Browser '{browser}' is not supported")

    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser type: chrome or firefox or edge")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")
