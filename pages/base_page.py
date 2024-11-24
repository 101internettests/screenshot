import time
# import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    __timeout = 10

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @staticmethod
    def highlight(element):
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=__timeout):
        try:
            element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            if element:
                self.highlight(element)
                return element
        except TimeoutException:
            return False

    def elements_are_visible(self, locator, timeout=__timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=__timeout):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=__timeout):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=__timeout):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=__timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # def go_to_element(self, locator, timeout=__timeout):
    #     return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def switch_handles_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_back_handles_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])