#!/usr/bin/env python

import pytest

from unittestzero import Assert
from pages.page_object import MySiteHomePage

xfail = pytest.mark.xfail
nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive


class TestTemplate(MySiteHomePage):

    def test_that_we_do_something_to_find_a_bug(self, mozwebqa):
        pass

    @nondestructive
    def test_that_we_do_something_to_find_a(self, mozwebqa):
        pass

    @destructive
    def test_that_we_do_something_to_find(self, mozwebqa):
        pass

    @xfail
    def test_that_we_do_something_to_(self, mozwebqa):
        pass
