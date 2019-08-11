import os
import unittest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BaseTest(unittest.TestCase):
    desired_caps = {}

    def android_driver(self):
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName'] = 'Nexus5X'
        self.desired_caps['appPackage'] = 'com.vida.healthcoach'
        self.desired_caps['appActivity'] = \
            'com.vida.healthcoach.StartupActivity'
        self.desired_caps['app'] = os.path\
            .abspath(os.path
                     .join(os.path
                           .dirname(__file__),
                           '../resources/app-distro-release.apk'))
        return webdriver.Remote('http://localhost:4723/wd/hub',
                                self.desired_caps)

    def ios_driver(self):
        self.desired_caps['platformName'] = 'iOS'
        self.desired_caps['platformVersion'] = '12.2'
        self.desired_caps['automationName'] = 'xcuitest'
        self.desired_caps['deviceName'] = 'iPhone XS Max'
        self.desired_caps['app'] = os.path\
            .abspath(os.path
                     .join(os.path
                           .dirname(__file__),
                           '../resources/Vida.app'))

        return webdriver.Remote('http://localhost:4723/wd/hub',
                                self.desired_caps)

    def setup_driver(self):
        self.driver: WebDriver = self.android_driver()
        self.driver.implicitly_wait(30)
        return self.driver

    def close_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    unittest.TextTestRunner(verbosity=2).run(suite)



