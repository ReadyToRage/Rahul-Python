from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class DragDrop:

    def __init__(self, driver):
        self.driver = driver

    def test_drag(self):

        self.driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollBy(0,300)")
        dd = self.driver.find_element(By.XPATH, "//*[text()='Progress Bar & Sliders']")
        dd.click()
        #scroll the window by using executescript
        self.driver.execute_script("window.scrollBy(0,200)")
        self.driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()
        assert "drag-drop-range-sliders-demo" in self.driver.current_url
        dragdrop = self.driver.find_element(By.XPATH, "//input[@type='range' and @value='15']")
        #using the Action class to work with sliders and drag and drop
        ActionChains(self.driver).drag_and_drop_by_offset(dragdrop, 100, 0).perform()
        self.driver.save_screenshot("C:\\Pycharmprojects\\Lamdatest\\screenshots\\test_drag.png")
        text=self.driver.find_element(By.XPATH,'//*[@id="rangeSuccess"]').text
        #assert the value
        if text=="95":
            assert True
        else:
            assert False
        print("TC Drag & Drop Sliders passed")
        self.driver.close()
