import unittest
from Utilities.base_test import BaseTest
from Data.data import Login_Data
from Pages.home_page import HomeScreen


class LoginTest(unittest.TestCase):
    driver = BaseTest().setup_driver()

    def test_login(self):
        self.username = Login_Data["username"]
        self.password = Login_Data["password"]
        home_page = HomeScreen(self.driver)
        self.assertTrue(home_page.click_login_button()
                        .set_email_text(self.username)
                        .set_password_text(self.password)
                        .click_login_button()
                        .close_alert_popup()
                        .check_now_tab_title_text())

    def teardown(self):
        self.driver.quit()


# ---START OF SCRIPT
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase (LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
