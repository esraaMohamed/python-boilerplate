from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.base_page import BasePage
from Pages.now_page import NowTabScreen


class LoginScreen(BasePage):

    def __init__(self, driver):
        super(self.__class__, self).__init__(driver)

    def set_email_text(self, email):
        """
        Setting email text value
        :param email:
        :return:
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.vida.healthcoach:id/login_email")))
        email_text_field = self.driver \
            .find_element_by_id("com.vida.healthcoach:id/login_email")
        email_text_field.send_keys(email)
        return LoginScreen(self.driver)

    def set_password_text(self, password):
        """
        Setting password text value
        :param password:
        :return:
        """
        WebDriverWait(self.driver, 5) \
            .until(EC.visibility_of_element_located(
            (MobileBy.ID, "com.vida.healthcoach:id/login_password")))
        password_text_field = self.driver \
            .find_element_by_id("com.vida.healthcoach:id/login_password")
        password_text_field.send_keys(password)
        return LoginScreen(self.driver)

    def click_login_button(self):
        """
        Click on the login button should return an object of Now Page Screen
        :param number:
        :return:
        """
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((
                MobileBy.ID, "com.vida.healthcoach:id/login_button")))
        login_button = self.driver\
            .find_element_by_id("com.vida.healthcoach:id/login_button")
        login_button.click()
        return NowTabScreen(self.driver)

