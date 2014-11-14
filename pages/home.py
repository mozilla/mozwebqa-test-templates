#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import datetime

from selenium.webdriver.common.by import By

from base import Base
from page import PageRegion


class HomePage(Base):
    """This Page Object models the QMO Home Page (https://quality.mozilla.org/)."""

    # The title of this page, which is used by is_the_current_page() in page.py
    _page_title = u'QMO \u2013 quality.mozilla.org | The Home of Mozilla QA'

    # Locators for the home page
    _tagline_locator = (By.ID, 'tagline')
    _news_items_locator = (By.TAG_NAME, 'article')

    # Link locators, which can be used for checking visibility, accuracy and validity of links
    teams_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#page-39 > a'),
            'url_suffix': '/teams/firefoxqe/',
        }, {
            'locator': (By.CSS_SELECTOR, '#page-40 > a'),
            'url_suffix': '/teams/web-qa/',
        }, {
            'locator': (By.CSS_SELECTOR, '#page-45493 > a'),
            'url_suffix': '/teams/services/',
        }, {
            'locator': (By.CSS_SELECTOR, '#page-45496 > a'),
            'url_suffix': '/teams/mobile/',
        }, {
            'locator': (By.CSS_SELECTOR, '#page-47307 > a'),
            'url_suffix': '/teams/firefox-os-qa/',
        },
    ]

    def go_to_page(self):
        """Open the home page."""
        self.open('/')

    @property
    def tagline(self):
        """Return the text of the tagline."""
        return self.find_element(self._tagline_locator).text

    @property
    def news_items_count(self):
        """Return the number of news items on the home page."""
        return len(self.find_elements(self._news_items_locator))

    @property
    def news_items(self):
        """Return a list of new items, each of which is a single news item from the home page."""
        return [self.NewsItem(self.testsetup, web_element)
                for web_element in self.find_elements(self._news_items_locator)]

    class NewsItem(PageRegion):
        """Allows each news item on the home page to be treated as a separate object."""

        _title_locator = (By.CSS_SELECTOR, 'h1 > a')
        _entry_posted_locator = (By.CSS_SELECTOR, 'p.entry-posted')
        _month_posted_locator = (By.CLASS_NAME, 'posted-month')
        _day_posted_locator = (By.CLASS_NAME, 'posted-date')
        _year_posted_locator = (By.CLASS_NAME, 'posted-year')

        @property
        def title(self):
            """Return the title of the news item."""
            return self.find_element(self._title_locator).text

        @property
        def is_post(self):
            """Return True if the item is a post (as opposed to an event)."""
            return self.is_element_present(self._entry_posted_locator)

        @property
        def date_posted(self):
            """Return the date posted as a Python date."""
            year = self.find_element(self._year_posted_locator).text
            month = self.find_element(self._month_posted_locator).text
            day = self.find_element(self._day_posted_locator).text
            time_struct = time.strptime(
                '%s %s %s' % (year, month, day),
                '%Y %b %d'
            )
            return datetime.date.fromtimestamp(time.mktime(time_struct))
