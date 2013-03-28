#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime

from BeautifulSoup import BeautifulStoneSoup    # Only required for the test that doesn't use Selenium
import pytest
import requests
from unittestzero import Assert

from pages.home import HomePage
from base_test import BaseTest


class TestHomePage(BaseTest):

    @pytest.mark.nondestructive
    def test_that_page_has_correct_tagline(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.equal('The home of Mozilla QA', home_page.tagline)

    @pytest.mark.nondestructive
    def test_that_page_has_news_items(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.greater(home_page.news_items_count, 0)

    @pytest.mark.nondestructive
    def test_that_news_items_are_sorted_in_reverse_chronological_order(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        news_items = home_page.news_items
        most_recent_date = datetime.date.today()
        for news_item in news_items:
            if news_item.is_post:
                news_item_date = news_item.date_posted
                Assert.greater_equal(most_recent_date, news_item_date, 'News items are out of sequence. %s is not after %s.' % (most_recent_date, news_item_date))
                most_recent_date = news_item_date

    # The following 3 tests check for visibilty, accuracy and validity of the team links on the home page
    @pytest.mark.nondestructive
    def test_that_getting_started_links_are_visible(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.getting_started_links_list:
            if not home_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_that_getting_started_link_destinations_are_correct(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.getting_started_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_that_getting_started_link_urls_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.getting_started_links_list:
            url = home_page.link_destination(link.get('locator'))
            response_code = self.get_response_code(url, mozwebqa.timeout)
            if response_code != requests.codes.ok:
                bad_links.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_links), '%s bad urls found: ' % len(bad_links) + ', '.join(bad_links))

    # This test checks the validity of all links on the page, and doesn't use Selenium
    # Note: for the purposes of example, this only checks the first 10 links
    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_checks_the_validity_of_all_links_on_the_page(self, mozwebqa):
        url = mozwebqa.base_url
        page_response = requests.get(url, verify=False)
        html = BeautifulStoneSoup(page_response.content)
        bad_links = []
        links = html.findAll('a')
        for index, link in enumerate(links[:10]):
            url = self.make_absolute(link['href'], mozwebqa.base_url)
            response_code = self.get_response_code(url, mozwebqa.timeout)
            if response_code != requests.codes.ok:
                bad_links.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_links), '%s bad urls found: ' % len(bad_links) + ', '.join(bad_links))
