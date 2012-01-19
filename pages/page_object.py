#!/usr/bin/env python

from selenium import selenium
from vars import ConnectionParameters
from page import Page


class MySiteHomePage(Page):

    _some_locator = 'id=someLocator'

    def __init__(self, selenium):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = selenium

    @property
    def item_on_page(self):
        return self._some_locator

    @property
    def get_page_title(self):
        return self.sel.get_title()

    def do_something_on_the_page(self):
        pass
