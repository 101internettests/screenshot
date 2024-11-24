import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    if os.getenv("HEADLESS") == "True":
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 4000)
    # driver.maximize_window()
    yield driver
    driver.quit()
