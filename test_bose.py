# from base import BaseTest
# from utilities import logger
# from utilities import report
# from utilities.screenshot import Screenshot
# from utilities import excelReader
# import logging
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from utilities.report import AllureReporter
# import allure
# from utilities.webDriverHelper import WebDriverHelper
# import time
# from selenium.webdriver.common.action_chains import ActionChains


# class TestTwo(BaseTest):
#     my_logger = logger.configure_logger()
#     reporter = AllureReporter()

#     def test_one(self):
#         driver = self.setUpDriver()
#         self.my_logger.info("Clicked Bose Ultra OpenEarbuds")
#         driver.get("https://www.boseapac.com/en_in/index.html")
#         hover_locator = (By.XPATH, "//span[text()='Headphones']")
#         wb_h = WebDriverHelper(driver)
#         wb_h.hoverOneElement(hover_locator)
#         click_wireless = driver.find_element(
#             By.XPATH, "//span[text()='Wireless']")
#         wb_h.js_scroll(
#             (By.XPATH, '//div[@id="ariaButtonLabelID"]//p[contains(text(),"Bose Ultra Open Earbuds")]'))
#         time.sleep(5)

#         wb_h.js_clickElement((
#             By.XPATH, '//div[@id="ariaButtonLabelID"]//p[contains(text(),"Bose Ultra Open Earbuds")]'))
#         wb_h.js_scroll((By.XPATH,'/html/body/footer/div[1]/div[1]/div/div/div[1]/div/div/a[2]'))
#         wb_h.js_clickElement((By.XPATH,'/html/body/footer/div[1]/div[1]/div/div/div[1]/div/div/a[2]'))

#         wb_h.switch_to_new_window()
#         assert driver.current_url in driver.current_url
#         driver.find_element(By.XPATH,"//span[text()='@Bose']")
    

#         Screenshot.capture_screenshot(driver,"bose")
#         driver.quit()
        

#     def test_two(self):
#         driver = self.setUpDriver()
#         driver.get("https://www.boseapac.com/en_in/index.html")
#         hover_locator = (
#             By.XPATH, "/html/body/header/div[3]/div/div[2]/div/div[2]/div/ul/li[2]/a/span")
#         wb_h = WebDriverHelper(driver)
#         wb_h.hoverOneElement(hover_locator)
#         # Click on Home AUdio
#         wb_h.js_clickElement((By.XPATH, "(//span[text()='Home Audio'])[1]"))
#         wb_h.js_scroll((By.XPATH,'/html/body/main/div/section/div/div[6]/div/div/section/div[1]/div/h3'))
#         wb_h.js_clickElement((By.XPATH,'(//div[@id="ariaButtonLabelID"])[6]'))
#         wb_h.js_scroll((By.XPATH,'/html/body/main/div[2]/div[3]/div/div/div[2]/div/div[5]/h2'))
#         Screenshot.capture_screenshot(driver,'FAQ_option')
#         driver.quit()

#     def test_three(self):
#         driver=self.setUpDriver()
#         driver.get("https://www.boseapac.com/en_in/index.html")
#         input_box=driver.find_element(By.XPATH,'//form/div/div[1]')
#         input_box.click()
#         input_search=driver.find_element(By.XPATH,'(//input)[2]')
#         input_search.send_keys("Bose Sport Earbuds")
#         time.sleep(3)
#         button_btn=driver.find_element(By.XPATH,'/html/body/header/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[2]/button')
#         button_btn.click()
#         result_title=driver.title.strip()
#         # assert result_title in "Bose Sport Earbuds"

#         driver.quit()
