#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests


class BaseTest:
    """A base test class that can be extended by other tests to include utility methods."""

    def get_response_code(self, url, timeout):
        """Return the response code for a get request to the specified url."""
        # this sets max_retries to 5
        requests.adapters.DEFAULT_RETRIES = 5
        try:
            r = requests.get(url, verify=False, allow_redirects=True, timeout=timeout)
            return r.status_code
        except requests.Timeout:
            return 408

    def make_absolute(self, url, base_url):
        """Return the url argument as an absolute url."""
        if url.startswith('http'):
            return url
        return base_url + url
