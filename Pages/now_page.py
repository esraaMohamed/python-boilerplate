from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.base_page import BasePage


class NowTabScreen(BasePage):

    def __init__(self, driver):
        super(self.__class__, self).__init__(driver)

    def close_alert_popup(self):
        """
        Setting email text value
        :param:
        :return object of the now tab screen:
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "android:id/button2")))
        later_button = self.driver \
            .find_element_by_id("android:id/button2")
        later_button.click()
        return NowTabScreen(self.driver)

    def check_now_tab_title_text(self):
        """
        Checking to see if the now tab screen title is valid
        :return boolean:
        """
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.vida.healthcoach:id/now_tab_title_text")))
        now_tab_title_text = self.driver \
            .find_element_by_id("com.vida.healthcoach:id/now_tab_title_text")
        now_tab_text = now_tab_title_text.text
        return NowTabScreen(now_tab_text == "Recommended for You")

