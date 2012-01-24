#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.page_object import MySiteHomePage


class TestXfail():

    @pytest.mark.xfail(reason='templates demo xfail')
    def test_load_baseurl_xfail(self, mozwebqa):
        '''
        Demo Test - Mark test failed if there known bug exist
        '''
        home_page = MySiteHomePage(mozwebqa)
        home_page.go_to_home_page()
        Assert.equal(home_page.header_text, 'BlaBla')

    @pytest.mark.xfail
    def test_that_we_do_something_to_find_a_bug(self, mozwebqa):
        pass
