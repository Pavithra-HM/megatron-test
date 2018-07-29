import unittest
from selenium.webdriver import Chrome
from lib.ui.loginpage import LoginPage

class TestLoginS137890P1(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome(
            (r"C:\Users\Admin\AppData\Local\Programs\Python\Python36-32\chromedriver_win32\chromedriver.exe"))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://demo.actitime.com')#localhost')
        self.login_page=LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_invalid_tc1238990(self):
        # Go to login page
        self.login_page.wait_for_login_page_to_load()
        # enter username
        self.login_page.get_username_textbox().send_keys("admin")
        #enter password
        self.login_page.get_password_textbox().send_keys('Invalid')
        #click on login button
        self.login_page.get_login_button().click()
        #get error message
        actual_error_message=self.login_page.get_login_error_msg().text
        expected_error_message='Username or Password is invalid. Please try again.'
        #Verify error message
        assert actual_error_message==expected_error_message