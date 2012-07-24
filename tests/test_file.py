#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.page_object import MySiteHomePage


class TestTemplate():

    @pytest.mark.nondestructive
    def test_load_baseurl_and_assert_header(self, mozwebqa):
        '''
        Demo Test - Verify Header is correct on Amo Page
        '''
        home_page = MySiteHomePage(mozwebqa)
        home_page.go_to_home_page()
        Assert.equal(home_page.header_text, 'We are')

    @pytest.mark.nondestructive
    def test_that_we_do_something_to_find_a_bug(self, mozwebqa):
        pass
