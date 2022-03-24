from selenium.webdriver.common.by import By




class SimpleForm:
    textbox_message_ID = "user-message"
    button_submit_ID = "showInput"
    Message_by_ID = "message"
    link_text = "Simple Form Demo"

    def __init__(self, driver):
        self.driver = driver

    def test_checktext(self,variable="Welcome to Lambdatest"):



       self.driver.get("https://www.lambdatest.com/selenium-playground")
       self.driver.find_element(By.LINK_TEXT,self.link_text).click()
       self.driver.find_element(By.ID,self.textbox_message_ID).send_keys(variable)
       self.driver.find_element(By.ID,self.button_submit_ID).click()
       text = self.driver.find_element(By.XPATH, "//*[@id='message']").text
       print(text)
       assert "Welcome to Lambdatest" in text
       self.driver.save_screenshot("C:\\Pycharmprojects\\Lamdatest\\screenshots\\test_checktext.png")
       print("TC SimpleForm passed")

       self.driver.close()




