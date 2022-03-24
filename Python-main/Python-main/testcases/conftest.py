import pytest

from selenium import webdriver

@pytest.fixture()
def test_driver():
    driver = webdriver.Remote(
        command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format("rdharanitharan5",
                                                                          "DDQ3Yek88zTulC4KhCvszmHKP5XPaDTHwx1sYbjWtmulxc1XBJ"),
        desired_capabilities={
            "build": 'PyunitTest sample build', "name": 'Py-unittest', "browserName": 'Chrome',
            "version": '92.0', "platform": 'Windows 10', "resolution": '1024x768',
            "console": 'true', "network": 'true'
        }
    )
    return driver


