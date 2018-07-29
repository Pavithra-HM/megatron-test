import pytest
from selenium.webdriver import Chrome, Firefox

def get_driver_instance():
    browser= pytest.config.option.type.lower()
    if browser=='chrome':
        driver=Chrome("./browser-server/chromedriver.exe")
    elif browser=='firefox':
        driver=Firefox("./browser-server/geckodriver.exe")
    else:
        print('Invalid Browser option')
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://localhost")
    return driver