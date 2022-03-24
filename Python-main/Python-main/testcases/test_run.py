from PageObjects.DragandDrop import DragDrop
from PageObjects.InputFormSubmit import InputForm
from PageObjects.SimpleFormDemo import SimpleForm
from utilities.logfile import LogGen


class Testclass:
    logger = LogGen.loggen()
#pytest -v -s --html=report.html --self-contained-html testcases/test_run.py
    def test_case01(self, test_driver):
        self.logger.info("**********Test Case One Started**********")
        self.driver = test_driver
        tc1 = SimpleForm(self.driver)
        tc1.test_checktext()

        self.logger.info("**********Test Case One Done**********")

    def test_case02(self, test_driver):
        self.logger.info("**********Test Case two Started**********")
        self.driver = test_driver
        tc2 = DragDrop(self.driver)
        tc2.test_drag()
        self.logger.info("**********Test Case two Done**********")

    def test_case03(self, test_driver):
        self.logger.info("**********Test Case three Started**********")
        self.driver = test_driver
        tc3 = InputForm(self.driver)
        tc3.test_form()
        tc3.test_validate()
        self.logger.info("**********Test Case three Done**********")
