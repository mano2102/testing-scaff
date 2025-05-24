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


# class TestOne(BaseTest):
#     my_logger = logger.configure_logger()
#     reporter = AllureReporter()

#     @allure.epic("PNG Jewellers Website Automation")
#     @allure.feature("Silver Bullion Selection")
#     @allure.story("Sort and List 24K Silver Bullion")
#     @allure.title("Verify 24K Silver Products Are Listed")
#     @allure.description("This test navigates to PNG Jewellers, selects 24K silver under bullions, sorts by price, and lists the product items.")
#     def test_one(self):
#         driver = self.setUpDriver()
#         try:
#             with allure.step("Opening PNG Jewellers website"):
#                 driver.get("https://www.pngjewellers.com/")
#                 self.my_logger.info("Getting the url")
#             with allure.step("Clicking on Bullions"):
#                 bullions = driver.find_element(
#                     By.XPATH, '//*[@id="Details-HeaderMenu-4"]/summary/a/span')
#                 bullions.click()
#                 self.my_logger.info("Clicked Bullions")
#             with allure.step("Selecting 24K Silver"):
#                 silver_24_k = driver.find_element(
#                     By.XPATH, '//*[@id="Facet-1-template--19361993785563__product-grid"]/fieldset/ul/li[1]/label/span[1]/span')
#                 silver_24_k.click()
#                 self.my_logger.info("Selecting 24K Silver")
#             with allure.step("Sorting by Price"):
#                 select_element = wait.until(EC.presence_of_element_located((By.ID, "sort-by")))
#                 select = Select(select_element)
#                 select.select_by_index(4)
#             with allure.step("Collecting Product Listings"):
#                 ul_container = driver.find_element(
#                     By.XPATH, '//ul[@id="product-grid"]')
#                 li_elements = ul_container.find_elements(By.TAG_NAME, 'li')
#                 logging.warning(f"Found {len(li_elements)} product items")
#                 scr_name = Screenshot.capture_screenshot(driver, "list")
#                 allure.attach.file(scr_name, name="24K Silver Listing Screenshot",
#                                    attachment_type=allure.attachment_type.PNG)
#         except Exception as e:
#             scr_name = Screenshot.capture_screenshot(driver, "test_one_error")
#             allure.attach.file(scr_name, name="24k_listing_error",
#                                attachment_type=allure.attachment_type.PNG)
#             raise e
#         finally:
#             self.reporter.generate_report()
#             driver.quit()

#     @allure.epic("PNG Jewellers Website Automation")
#     @allure.feature("Gold Jewellery Navigation")
#     @allure.story("Filter Party Wear Products")
#     @allure.title("Verify 'Party Wear' Page Title After Navigation")
#     @allure.description("This test hovers over the Gold menu, clicks on 'Party Wear', sets the price filter, and checks the page title.")
#     def test_two(self):
#         driver = self.setUpDriver()
#         self.my_logger.warning("Test 2 is running")
#         wb_h = WebDriverHelper(driver)

#         try:
#             with allure.step("Opening PNG Jewellers website"):
#                 driver.get("https://www.pngjewellers.com/")

#             with allure.step("Hovering on Gold menu"):
#                 locator = (
#                     By.XPATH, '//*[@id="Details-HeaderMenu-3"]/summary/a/span')
#                 wb_h.hoverOneElement(locator)
#                 self.my_logger.info("Hovered on the Gold menu")

#             with allure.step("Clicking on Party Wear link"):
#                 party_wear = driver.find_element(
#                     By.XPATH, '//*[@id="MegaMenu-Content-2"]/ul/li[1]/div/ul/div/div/div[2]/div/div[3]/div[1]/a')
#                 party_wear.click()

#             with allure.step("Setting price filter to 10000"):
#                 from_input_box = driver.find_element(
#                     By.XPATH, '//*[@id="Filter-Price-GTE"]')
#                 driver.execute_script(
#                     "arguments[0].scrollIntoView(true);", from_input_box)
#                 from_input_box.send_keys('10000')
#                 time.sleep(3)

#             with allure.step("Validating page title"):
#                 page_title = driver.title.strip()
#                 allure.attach(page_title, name="Page Title",
#                               attachment_type=allure.attachment_type.TEXT)
#                 assert "Party Wear" in page_title, f"'Party Wear' not found in page title: {page_title}"

#         except Exception as e:
#             screenshot_path = Screenshot.capture_screenshot(
#                 driver, "test_two_error")
#             allure.attach.file(screenshot_path, name="test_two_error",
#                                attachment_type=allure.attachment_type.PNG)
#             raise e

#         finally:
#             self.my_logger.warning("Test 2 is quitting")
#             self.reporter.generate_report()
#             driver.quit()


#     @allure.epic("PNG Jewellers Website Automation")
#     @allure.feature("Store Locator")
#     @allure.story("Sort and List 24K Silver Bullion")
#     @allure.title("Verify 24K Silver Products Are Listed")
#     @allure.description("This test navigates to PNG Jewellers, selects 24K silver under bullions, sorts by price, and lists the product items.")
#     def test_three(self):
#         driver = self.setUpDriver()
#         self.my_logger.warning(" Test 3 is running")
#         wb_h = WebDriverHelper(driver)
#         driver.get("https://www.pngjewellers.com/")
#         driver.find_element(
#             By.XPATH, "(//span[text()='Store Locator'])[1]").click()
#         main_window = driver.current_window_handle
#         all_windows = driver.window_handles

#     # Step 5: Switch to the new window
#         for window in all_windows:
#             if window != main_window:
#                 driver.switch_to.window(window)
#                 break
#         element_to_scroll = driver.find_element(By.XPATH, '//input[@id="address_search"]')
#         driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
#         element_to_scroll.send_keys("641042")
#         search_button=driver.find_element(By.XPATH,'//button[@id="submitBtn"]')
#         time.sleep(5)
#         search_button.click()
#         time.sleep(5)
#         # h3_elements = driver.find_elements(By.XPATH, "//ul/li/a/h3")

#         # for i in range(len(h3_elements)):
#         #     self.my_logger.info(i)

#         for i in range(1, 6):  # Usually XPath indices start from 1
#             dynamic_xpath = f'//*[@id="sl_addresses"]/li[{i}]/a/h3'
#             driver.find_element(By.XPATH,dynamic_xpath)
#             self.my_logger.info(dynamic_xpath)




#         self.my_logger.error(" is running")
#         self.my_logger.warning("Test 3  is quitting")
#         driver.quit()
