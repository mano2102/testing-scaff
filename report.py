import os
import datetime
import time


class AllureReporter:
    BASE_DIRECTORY = "/home/coder/project/workspace/Project/Report"
    RESULTS_DIRECTORY = os.path.join(BASE_DIRECTORY, "Allure")
    REPORT_DIRECTORY = os.path.join(BASE_DIRECTORY, "AllureReports")

    def __init__(self):
        time.sleep(2)
        os.makedirs(self.RESULTS_DIRECTORY, exist_ok=True)
        os.makedirs(self.REPORT_DIRECTORY, exist_ok=True)

    def generate_report(self):
        time.sleep(2)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        timestamped_folder = os.path.join(
            self.REPORT_DIRECTORY, f"AllureReports_{timestamp}")
        allure_command = f"allure generate {self.RESULTS_DIRECTORY} -o {timestamped_folder}"
        os.system(allure_command)
