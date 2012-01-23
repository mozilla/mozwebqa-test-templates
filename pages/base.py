#!/usr/bin/env python

from selenium.webdriver.support.ui import WebDriverWait

from pages.page import Page


class Base(Page):
    '''
    Base class for global project specific functions
    '''
    @property
    def page_title(self):
        WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        return self.selenium.title

    def go_to_home_page(self):
        self.selenium.get(self.base_url)
