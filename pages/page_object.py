#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import Base
from page import Page


class MySiteHomePage(Base):

    _some_locator_by_id = (By.ID, 'someLocator')
    _some_locator_by_css = (By.CSS_SELECTOR, '#someLocator')
    _some_locator_by_xpath = (By.XPATH, "//div[@id='someLocator']")
    _some_elements_locator = (By.CSS_SELECTOR, 'li .someElementsLocator')

    # Demo locators
    _page_title = u"Mozilla \u2014 Home of the Mozilla Project \u2014 mozilla.org"
    _header_locator = (By.CSS_SELECTOR, 'h1')

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

    def news_item(self, lookup):
        return self.NewsList(self.testsetup, lookup)

    class NewsList(Page):
        _home_news_locator = (By.CSS_SELECTOR, '#home-news-list li')
        _link_locator = (By.CSS_SELECTOR, 'a')

        def __init__(self, testsetup, lookup):
            Page.__init__(self, testsetup)
            self._root_element = self.selenium.find_element(By.CSS_SELECTOR,
                                          "%s:nth-child(%s)" % (self._home_news_locator[1], lookup))

        @property
        def name(self):
            return self._root_element.text

        def click_link(self):
            self._root_element.find_element(*self._link_locator).click()
