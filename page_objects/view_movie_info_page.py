from selenium.webdriver.support.wait import WebDriverWait

from utilities.base_class import BaseClass


class ViewMovieInfoPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    layout_class = ".layout_lists__rBjPn"

