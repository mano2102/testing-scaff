# from base import BaseTest
# from utilities import logger
# from utilities import report
# from utilities.screenshot import Screenshot
# from utilities import excelReader
# import logging
# from selenium.webdriver.common.by import By


# class TestGoogle(BaseTest):
#     logger.configure_logger()
#     url = 'https://practicetestautomation.com/practice-test-login/'

#     def test_one(self):
#         driver = self.setUpDriver()
#         driver.get(self.url)
#         # logging.debug(driver+" something wrong with the driver")

#         logging.info("test_one")
#         username = driver.find_element(By.XPATH, '//input[@id="username"]')
#         username.send_keys("student")
#         password = driver.find_element(By.XPATH, '//input[@id="password"]')
#         password.send_keys("Password123")
#         driver.execute_script("window.scrollBy(0, 100);")
#         login_button = driver.find_element(By.XPATH, '//button[@id="submit"]')
#         login_button.click()

#         # Screenshot.capture_screenshot(driver, "sample")
#         try:
#             driver.close()
#             driver.quit()
#         except Exception as e:
#             print("Driver closing is not success",e)
