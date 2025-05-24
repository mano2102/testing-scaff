from base import BaseTest
from utilities import logger
from utilities import report
from utilities.screenshot import Screenshot
from utilities import excelReader
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.report import AllureReporter
import allure
from utilities.webDriverHelper import WebDriverHelper
import time
from selenium.webdriver.common.action_chains import ActionChains


class TestTwo(BaseTest):
    my_logger = logger.configure_logger()
    reporter = AllureReporter()
    url = 'https://www.purplle.com/.'

    def test_one(self):
        driver = self.setUpDriver()
        self.my_logger.info("Clicked Bose Ultra OpenEarbuds")
        driver.get(self.url)
        wbh = WebDriverHelper(driver)
        wbh.hoverOneElement(
            (By.XPATH, '//*[@id="body"]/app-root/div/div/app-header/header/div[3]/div/div/div[2]/div[2]/a'))
        wbh.sendKeys(
            (By.XPATH, '//*[@id="body"]/app-root/div/div/app-header/header/div[3]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/input'), 'lakme')
        time.sleep(5)
        lakme_loc = (By.XPATH, '//a[@id="Lakme"]')
        wbh.js_clickElement(lakme_loc)
        lakme_first_loc = (By.XPATH,
                           '//*[@id="swiper-wrapper-dcc6265617d1310c5"]/div[1]/div/div/div[2]/div[1]')
        wbh.js_clickElement(lakme_first_loc)

        glycolic_loc=(By.XPATH,"//span[text()='Glycolic']")
        wbh.js_clickElement(glycolic_loc)
        gm_50_loc=(By.XPATH,"//span[text()='50 gm']")
        wbh.js_clickElement(gm_50_loc)
        



        driver.quit()

    def test_two(self):
        driver = self.setUpDriver()
        driver.get(self.url)

        driver.quit()

    def test_three(self):
        driver = self.setUpDriver()
        driver.get(self.url)

        driver.quit()
