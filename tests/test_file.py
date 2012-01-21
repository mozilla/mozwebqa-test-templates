#!/usr/bin/env python

import pytest

from unittestzero import Assert
from pages.page_object import MySiteHomePage

xfail = pytest.mark.xfail
nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive


class TestTemplate():

    def test_load_amo_assert_header(self, mozwebqa):
        '''
        Demo Test - Verify Header is correct on Amo Page
        '''
        home_page = MySiteHomePage(mozwebqa)
        Assert.equal(home_page.amo_header, 'ADD-ONS')

    @xfail(reason='templates demo xfail')
    def test_load_amo_xfail(self, mozwebqa):
        '''
        Demo Test - Mark test failed if there known bug exist
        '''
        home_page = MySiteHomePage(mozwebqa)
        Assert.equal(home_page.amo_header, 'BlaBla')

    @nondestructive
    def test_that_we_do_something_to_find_a(self, mozwebqa):
        pass

    @destructive
    def test_that_we_do_something_to_find(self, mozwebqa):
        pass
