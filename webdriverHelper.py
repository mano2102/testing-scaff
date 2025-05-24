import traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from utilities.eventHandler import EventHandler

class WebDriverHelper:
    def __init__(self, driver):
        self.driver = driver

    def openPage(self, url):
        try:
            self.driver.get(url)
        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in " + str(e))

    def clickElement(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            element.click()

        except WebDriverException as e:
            print(e)
            raise Exception("Error in " + str(e))

    def sendKeys(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))

            element.send_keys(text)

        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in " + str(e))

    def hoverOneElement(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))

            ActionChains(self.driver).move_to_element(element).perform()
            eh=EventHandler()
            eh.log_hover(element)
        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in " + str(e))

    def hoverTwoElements(self, firstLocator, secondLocator):
        try:
            firstElement = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(firstLocator))
            secondElement = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(secondLocator))

            actions = ActionChains(self.driver)
            actions.move_to_element(firstElement).move_to_element(
                secondElement).perform()

        except WebDriverException as e:
            traceback.print_exc()
            raise Exception("Error in " + str(e))

    def js_scroll(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))

            self.driver.execute_script(
                "arguments[0].scrollIntoView();", element)

        except Exception as e:
            print(f'An Error occured: {e}')

    def js_clickElement(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator))

            self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            print(f'An Error ocured: {e}')

    def switch_to_new_window(self):
        try:
            all_win = self.driver.window_handles
            new_win = all_win[-1]
            self.driver.switch_to.window(new_win)

        except Exception as e:
            print(f'An Error ocured: {e}')

    def switch_to_frame(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            self.driver.switch_to.frame(element)

        except Exception as e:
            print(f'An Error ocured: {e}')

    def send_text_enter(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))

            element.send_keys(text)
            element.send_keys(Keys.ENTER)

        except Exception as e:
            print(f'An Error ocured: {e}')

    def hoverOneElement_click(self, firstLocator, secondLocator):
        try:
            element_1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(firstLocator))

            ActionChains(self.driver).move_to_element(element_1).perform()

            element_2 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(secondLocator))

            element_2.click()

        except Exception as e:
            print(f'An Error ocured: {e}')

    def hoverTwoElements_click(self, firstLocator, secondLocator, thirdlocator):
        try:
            firstElement = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(firstLocator))
            secondElement = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(secondLocator))

            actions = ActionChains(self.driver)
            actions.move_to_element(firstElement).move_to_element(
                secondElement).perform()

            thirdElement = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(thirdlocator))
            thirdElement.click()

        except Exception as e:
            print(f'An Error ocured: {e}')
