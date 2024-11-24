import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage
from locators.screen_page_locator import TestsSeoCheck

HEADLESS = os.getenv("HEADLESS") == "True"


class PageSeoCheck(BasePage):
    def _click_if_exists(self):
        try:
            self.scroll()
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TestsSeoCheck.READ_MORE_BUTTON_FIRST)
            )
            button.click()
            print("Clicked on the button")
        except NoSuchElementException:
            print("Button not found")
        except TimeoutException:
            print("Waiting for the button to become clickable timed out")
        except Exception as e:
            print(f"Error clicking the button: {e}")

    def scroll(self):
        try:
            time.sleep(2)
            scroll_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TestsSeoCheck.SCROLL_ONE)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
                                       scroll_element)
            print("Scrolled to the element")

            time.sleep(1)

        except TimeoutException:
            print("Timed out waiting for the scroll target element to become visible")
        except Exception as e:
            print(f"Error scrolling to element: {e}")