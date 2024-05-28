import pytest
from selenium import webdriver
from config.config_reader import config_reader


@pytest.fixture(scope="class")
def setUp(request):
    browser = config_reader.get('Settings', 'BROWSER')
    headless = config_reader.getboolean('Settings', 'HEADLESS')

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Edge()
        print("Launching Edge browser")
    else:
        raise ValueError(f"Browser '{browser}' is not supported")

    driver.maximize_window()
    driver.get(config_reader.get('Settings', 'BASE_URL'))

    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser type: chrome or firefox or edge")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")
