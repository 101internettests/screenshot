import os
import uuid
import time
from pages.screen_page import PageSeoCheck

HEADLESS = os.getenv("HEADLESS") == "True"


class TestSearChrome:
    def test_check_search_chrome(self, driver):
        if HEADLESS:
            driver.set_window_size(1920, 1080)
        else:
            driver.maximize_window()

        urls = [
            "https://piter-online.net/"
        ]
        names = [
            "Главная"
        ]

        for screen, name in zip(urls, names):
            try:
                uuid4 = uuid.uuid4()
                tags = PageSeoCheck(driver, screen)

                tags._click_if_exists()

                driver.get(screen)
                time.sleep(2)
                driver.execute_cdp_cmd('Page.enable', {})
                driver.execute_cdp_cmd('Page.setDeviceMetricsOverride', {
                    'width': 1920,
                    'height': 6000,
                    'deviceScaleFactor': 1,
                    'mobile': False,
                    'fitWindow': False
                })

                time.sleep(1)
                screenshot_path = f'C:/Users/Katerina/Desktop/screens/{name}.png'
                driver.save_screenshot(screenshot_path)
                print(f"Скриншот сохранен: {screenshot_path}")

            except Exception as e:
                print(f"Ошибка при работе с {screen}: {e}")