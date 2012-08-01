#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.page_object import MySiteHomePage


class TestNonDestructive():

    @pytest.mark.nondestructive
    def test_load_baseurl_nondestructive(self, mozwebqa):
        """
        This test is nondestructive - it does not write
        to the database or leave a mark on the website
        """
        home_page = MySiteHomePage(mozwebqa)
        home_page.go_to_home_page()
        Assert.true(home_page.is_the_current_page)

    def test_load_baseurl_destructive(self, mozwebqa):
        """
        This test is *not* marked as nondestructive and
        will be automatically skipped when run against
        a sensitive (ie Production) URL
        """
        pass
