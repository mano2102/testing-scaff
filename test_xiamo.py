import time
import allure
from selenium.webdriver import Keys
from base import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.screenshot import Screenshot
from utilities.webDriverHelper import WebDriverHelper
import logging
from utilities import logger


class Test_Page(BaseTest):
    # driver=Nan
    my_logger = logger.configure_logger()

    def setUp(self):
        url = "https://www.mi.com/in"
        self.driver = self.setUpDriver()
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # @pytest.mark.smoke
    # def test_method_name(self):
    #     pass

    def test_one(self):
        wbh= WebDriverHelper(self.driver)
        # self.driver.find_element(By.XPATH,'//*[@id="root"]/header/nav/div[1]/div[2]/nav/div[2]/div[1]/div/a/span').click()
        # hover the phones
        wbh.hoverOneElement((By.XPATH,'//*[@id="root"]/header/nav/div[1]/div[2]/nav/div[2]/div[1]/div/a/span'))
        # Hover the redmi phones
        wbh.hoverOneElement((By.XPATH,'//*[@id="root"]/header/nav/div[1]/div[2]/nav/div[2]/div[2]/div/div/div/div/div/div/ul/li[2]/div[1]/a[1]'))
        # Click on accessories
        wbh.clickElement((By.XPATH,'//*[@id="root"]/header/nav/div[1]/div[2]/nav/div[2]/div[2]/div/div/div/div/div/div/ul/li[2]/div[2]/div/div[2]/div/a[1]/span'))
        # CLick on sale
        wbh.clickElement((By.XPATH,'//*[@id="root"]/main/div/div[1]/ul/li[8]/div/div/span'))

        # Click buynow on the first mobile
        wbh.clickElement((By.XPATH,"//span[text()='Buy now']"))
        self.my_logger.info("Clicked the Buy Now")

        #Take the screenshot
        Screenshot.capture_screenshot(self.driver,"buy_now_product")

    # def test_two(self):
    #     # Scroll down to bottom
    #     wbh = WebDriverHelper(self.driver)
    #     self.driver.execute_script(
    #         "window.scrollTo(0, document.body.scrollHeight);")
    #     wbh.clickElement(
    #         (By.XPATH, '//*[@id="root"]/footer/div/div/section[1]/nav/div[1]/div/ul/li[12]/a'))
    #     time.sleep(3)
    #     wbh.switch_to_new_window()
    #     # click on the div to show the input
    #     # wbh.clickElement(
    #     #     (By.XPATH, '//*[@id="root"]/main/div/section[1]/div/form/div[2]/div[1]/div/div'))
    #     # Enter the values AS 600018 AND GIVE ENTER
    #     time.sleep(3)
    #     pincode = self.driver.find_element(
    #         By.XPATH, '//*[@id="root"]/main/div/section[1]/div/form/div[2]/div[1]/div/div/input')
    #     pincode.send_keys("600018")
    #     pincode.send_keys(Keys.ENTER)

    # def test_three(self):
    #     wbh = WebDriverHelper(self.driver)
    #     # Click on the profile
    #     wbh.clickElement((By.XPATH,'//*[@id="root"]/header/nav/div[2]/ul[2]/li[3]/section/button'))
    #     # Navigate to the login page
    #     wbh.sendKeys((By.XPATH,'//input[@name="account"]'),"sample@gmail.com")
    #     wbh.sendKeys((By.XPATH,'//input[@name="password"]'),"Sample@123")
    #     self.my_logger.info("Clicked the Buy Now")
    #     wbh.clickElement((By.XPATH,'//*[@id="rc-tabs-0-panel-login"]/form/div[1]/button'))
        
