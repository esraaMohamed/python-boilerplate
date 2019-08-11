from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_page import BasePage
from Pages.login_page import LoginScreen


class HomeScreen(BasePage):

    def __init__(self, driver):
        super(self.__class__, self).__init__(driver)

    def click_login_button(self):
        """
        Click on the login button should return an object of Login Screen
        :param:
        :return:
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.vida.healthcoach:id/startup_login_button")))
        login_button = self.driver\
            .find_element_by_id("com.vida.healthcoach:id/startup_login_button")
        login_button.click()
        return LoginScreen(self.driver)

    def click_get_started_button(self):
        """
        Click on the login button should return an object of Login Screen
        :param:
        :return:
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID,
                "com.vida.healthcoach:id/startup_get_started_button")))
        get_started_button = self.driver\
            .find_element_by_id(
            "com.vida.healthcoach:id/startup_get_started_button")
        get_started_button.click()
