#!/usr/bin/env python

from selenium.webdriver.common.by import By

from base import Base
from page import Page


class MySiteHomePage(Base):

    _some_locator_by_id = (By.ID, 'someLocator')
    _some_locator_by_css = (By.CSS_SELECTOR, '#someLocator')
    _some_locator_by_xpath = (By.XPATH, "//div[@id='someLocator']")
    _some_elements_locator = (By.CSS_SELECTOR, 'li .someElementsLocator')

    # Demo locators
    _page_title = "Home of the Mozilla Project"
    _header_locator = (By.CSS_SELECTOR, '#header h1 a')

    @property
    def header_text(self):
        return self.selenium.find_element(*self._header_locator).text

    @property
    def element_attribute(self):
        return self.selenium.find_element(*self._some_locator_by_id).get_attribute('someAttribute')

    @property
    def elements_count(self):
        return len(self.selenium.find_elements(*self._some_locator_by_id))

    def click_on_element(self):
        self.selenium.find_element(*self._some_locator_by_id).click()

    @property
    def elements(self):
        return [self.ElementsList(self.testsetup, element)
                for element in self.selenium.find_elements(*self._some_elements_locator)]

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
