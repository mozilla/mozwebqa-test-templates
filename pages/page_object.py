#!/usr/bin/env python

from selenium.webdriver.common.by import By

from base import Base
from page import Page


class MySiteHomePage(Base):

    _some_locator_by_id = (By.ID, 'someLocator')
    _some_locator_by_css = (By.CSS_SELECTOR, '#someLocator')
    _some_locator_by_xpath = (By.XPATH, "//div[@id='someLocator']")

    # Demo locators
    _amo_header_locator = (By.CSS_SELECTOR, '.site-title a')

    def __init__(self, testsetup, open_url=True):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        Base.__init__(self, testsetup)
        if open_url:
            self.selenium.get(self.base_url)

    @property
    def amo_header_text(self):
        return self.selenium.find_element(*self._amo_header_locator).text

    @property
    def element_attribute(self):
        return self.selenium.find_element(*self._some_locator_by_id).get_attribute('someAttribute')

    @property
    def elements_count(self):
        return len(self.selenium.find_elements(*self._some_locator_by_css))

    def click_on_element(self):
        self.selenium.find_element(*self._some_locator_by_xpath).click()

    @property
    def elements_list(self):
        return [self.ElementsList(self.testsetup, element)
                for element in self.selenium.find_elements(*self._elements_list_locator)]

    class ElementsList(Page):
        _link_locator = (By.CSS_SELECTOR, 'a')

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            return self._root_element.text

        def click_link(self):
            self._root_element.find_element(*self._link_locator).click()
