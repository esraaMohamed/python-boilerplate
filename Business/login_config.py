from Data.data import Login_Data
from Pages.home_page import HomeScreen
from Pages.login_page import LoginScreen


class LoginConfig():
    def __init__(self, driver):
        self.home_page = HomeScreen(driver)
        self.login_page = LoginScreen(driver)
        self.username = Login_Data["username"]
        self.password = Login_Data["password"]

    def login(self):
        self.home_page.click_login_button().set_email_text(self.username)\
            .set_password_text(self.password).click_login_button()
