#!/usr/bin/env python

from selenium import selenium
from vars import ConnectionParameters
import unittest
from page_object import MySiteHomePage


class TestTemplate(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(ConnectionParameters.server, ConnectionParameters.port,
                    ConnectionParameters.browser, ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConncetionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

    def test_that_we_do_something_to_find_a_bug(self):
        pass

if __name__ == "__main__":
    unittest.main()
