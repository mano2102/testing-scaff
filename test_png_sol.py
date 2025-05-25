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
    url = "https://www.pngjewellers.com/"

    # def test_01_one(self):
    #     driver = self.setUpDriver()
    #     self.my_logger.info("Clicked Bose Ultra OpenEarbuds")
    #     wbh = WebDriverHelper(driver)
    #     driver.get(self.url)
    #     diamnond_loc=(By.XPATH,'//*[@id="Details-HeaderMenu-2"]/summary/a/span')
    #     wbh.hoverOneElement(diamnond_loc)
    #     rings_loc=(By.XPATH,'//*[@id="MegaMenu-Content-1"]/ul/li[2]/div/a')
    #     wbh.hoverOneElement(rings_loc)
    #     diam_eng_rings_loc=(By.XPATH,'//*[@id="MegaMenu-Content-1"]/ul/li[2]/div/ul/div/div/div[1]/div/div[1]/div[2]/div[1]/a')
    #     wbh.clickElement(diam_eng_rings_loc)
    #     scroll_to_more_filter_loc=(By.XPATH,'//*[@id="Facet-8-template--19586656993499__product-grid"]/fieldset/ul/li[4]/label/span[1]/span')

    #     wbh.js_scroll(scroll_to_more_filter_loc)
    #     wbh.js_clickElement(scroll_to_more_filter_loc)
    #     first_product_loc=(By.XPATH,'//*[@id="CardLink-template--19586656993499__product-grid-8891584086235"]')
    #     wbh.js_clickElement(first_product_loc)
    #     assert driver.find_element(By.XPATH,'//*[@id="template--19586658533595__main-2-0"]').text.strip() in 'FG-VVS'
    #     Screenshot.capture_screenshot(driver,'product_fg_vvs')
    #     for i in range(0,300):
    #         self.my_logger.info("INFO")
    #     driver.quit()

    def test_02_two(self):
        driver = self.setUpDriver()
        driver.get(self.url)
        wbh = WebDriverHelper(driver)
        store_loca_loc=(By.XPATH,"(//a[@target='_blank'])[1]")
        wbh.clickElement(store_loca_loc)
        wbh.switch_to_new_window()
        scroll_to_store_input_loc=(By.XPATH,'//*[@id="address_search"]')
        wbh.js_scroll(scroll_to_store_input_loc)
        wbh.sendKeys(locator=scroll_to_store_input_loc,text="400001")
        self.my_logger.info("Pincode Entered : 400001")
        time.sleep(3)
        search_button_loc=(By.XPATH,'//*[@id="submitBtn"]')
        wbh.js_clickElement(search_button_loc)
        time.sleep(3)
        store_names = driver.find_elements(By.XPATH, '//*[@id="sl_addresses"]/li/a/h3')
        for i in range(len(store_names)):
            self.my_logger.info("Store " + str(i) + " " + store_names[i].text.strip())

        driver.quit()

    # def test_03_three(self):
    #     driver = self.setUpDriver()
    #     driver.get(self.url)
    #     wbh = WebDriverHelper(driver)
    #     life_style_loc = (By.XPATH, '//*[@id="brand-tab-pnglite"]/a/img')
    #     wbh.clickElement(life_style_loc)
    #     all_life_style_loc=(By.XPATH,'//*[@id="HeaderMenu-all-litestyle-jewellery"]/span')
    #     wbh.js_clickElement(all_life_style_loc)
    #     dropdown_element = driver.find_element(
    #         By.XPATH, '//select[@id="SortBy"]')

    #     # Wrap it with the Select class
    #     dropdown = Select(dropdown_element)
    #     dropdown.select_by_value("price-ascending")

    #     # price_text=driver.find_element(By.XPATH,'//*[@id="product-grid"]/li[1]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/span[2]').text

    #     # cleaned_price = int(price_text.replace("From Rs. ", "").replace(",", ""))


    #     # assert cleaned_price > 100000
    #     first_product_text=driver.find_element(By.XPATH,'(//a[@id="CardLink-template--19586656993499__product-grid-8870867828955"])[2]').text
    #     assert first_product_text.strip in "old Stud Gold Earring For Kids"
    #     Screenshot.capture_screenshot(driver,'gold_earring_kids')

    #     driver.quit()
