from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from test.functional.selenium_controller.web_controller import *

class Browser (object):

    base_url = 'http://127.0.0.1:8000/'
    binary = FirefoxBinary(settings.MOZILLA_FIREFOX_TEST_PATH)
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = True
    driver = webdriver.Firefox(firefox_binary=binary,executable_path=settings.SELENIUM_GECKODRIVER_MOZILLA,capabilities=capabilities)

    def visit (self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def tryLogg (self,email='',password=''):
        webController = DjangoWebTest()
        webController.login(email,password)

