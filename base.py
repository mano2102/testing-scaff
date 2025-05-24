import unittest
import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.eventHandler import EventHandler
import os
from utilities.report import AllureReporter

class BaseTest(unittest.TestCase):
    def setUpDriver(self):
        event_handler = EventHandler()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        remote_url = "http://localhost:4444"
        driver = webdriver.Remote(command_executor=remote_url, options=options)

        event_driver = EventFiringWebDriver(driver, event_handler)
        return event_driver

    if __name__ == '__main__':
        exit_code = pytest.main(['-v', '--alluredir=Report/Allure'])
        if exit_code == 0:
            reporter = AllureReporter()
            reporter.generate_report()
        else:
            print("Tests failed. Allure report not generated.")


# if __name__ == '__main__':
#     current_directory = os.path.dirname(os.path.abspath(__file__))
#     tests_directory = os.path.join(current_directory, 'tests')
#     allure_results_directory = os.path.join(current_directory, 'Report', 'Allure')
#     exit_code = pytest.main(['-v', tests_directory, '--alluredir', allure_results_directory])
#     html_report_directory = os.path.join(current_directory, 'Report', 'AllureReport')
#     if exit_code == 0:
#         allure_reporter = AllureReporter()
#         report_folder = allure_reporter.generate_report()
#         print(f"Allure report generated at: {report_folder}")
#     else:
#         print("Tests failed. Allure report not generated.")
