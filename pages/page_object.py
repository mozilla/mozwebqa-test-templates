#!/usr/bin/env python

from selenium.webdriver.common.by import By

from pages.base import Base


class MySiteHomePage(Base):

    _some_locator_by_id = (By.ID, 'someLocator')
    _some_locator_by_css = (By.CSS_SELECTOR, '#someLocator')
    _some_locator_by_xpath = (By.XPATH, "//div[@id='someLocator']")

    def __init__(self, testsetup, open_url=True):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        Base.__init__(self, testsetup)
        if open_url:
            self.selenium.get(self.base_url)

    @property
    def page_title(self):
        return self.selenium.title

    @property
    def element_text(self):
        return self.selenium.find_element(*self._some_locator_by_id).text

    @property
    def element_attribute(self):
        return self.selenium.find_element(*self._some_locator_by_id).get_attribute('someAttribute')

    @property
    def elements_count(self):
        return len(self.selenium.find_elements(*self._some_locator_by_css))

    def click_on_element(self):
        self.selenium.find_element(*self._some_locator_by_xpath).click()

    def do_something_on_the_page(self):
        pass
