import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class InputForm:
    username_by_ID = "name"
    email_by_ID = "inputEmail4"
    password_by_ID = "inputPassword4"
    company_by_ID = "company"
    website_by_ID = "websitename"
    city_by_ID = "inputCity"
    address1_by_ID = "inputAddress1"
    address2_by_ID = "inputAddress2"
    state_by_ID = "inputState"
    zip_by_ID = "inputZip"


    def __init__(self, driver):
        self.driver = driver

    def test_form(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo")
        self.driver.find_element(By.XPATH,'//*[text()="Input Forms"]').click()
        self.driver.execute_script("window.scrollBy(0,200)", "")
        self.driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.username_by_ID).send_keys("Rahul")
        self.driver.find_element(By.ID, self.email_by_ID).send_keys("rahul@gmail.com")
        self.driver.find_element(By.ID, self.password_by_ID).send_keys("@#%^GH")
        self.driver.find_element(By.ID, self.company_by_ID).send_keys("Microsoft")
        self.driver.find_element(By.ID, self.website_by_ID).send_keys("microsoft.com")
        # Using the SELECT class to work with dropdown
        country = self.driver.find_element(By.NAME,"country")
        c = Select(country)
        c.select_by_visible_text("United States")

        self.driver.find_element(By.ID, self.city_by_ID).send_keys("California")
        self.driver.find_element(By.ID, self.address1_by_ID).send_keys("PUB ROAD,CA,USA")
        self.driver.find_element(By.ID, self.address2_by_ID).send_keys("Streetbackpark,CA,USA")
        self.driver.find_element(By.ID, self.state_by_ID).send_keys("USA")
        self.driver.find_element(By.ID, self.zip_by_ID).send_keys("532672")

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[text()='Submit']").click()
        self.driver.save_screenshot("C:\\Pycharmprojects\\Lamdatest\\screenshots\\test_form.png")

    def test_validate(self):
        text = self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/section[3]/div/div/div[2]/div/p").text
        print(text)
        assert "Thanks for contacting us, we will get back to you shortly." in text
        print("TC InputForm passed")
        self.driver.close()
