#!/usr/bin/env python


import re
import time
import vars
import base64

page_load_timeout = vars.ConnectionParameters.page_load_timeout
base_url = vars.ConnectionParameters.baseurl
http_regex = re.compile('https?://((\w+\.)+\w+\.\w+)')


class Page(object):
    '''
    Base class for all Pages
    '''

    def __init__(self, selenium):
        '''
        Constructor
        '''
        self.selenium = selenium

    @property
    def is_the_current_page(self):
        page_title = self.selenium.get_title()
        if not page_title == self._page_title:
            self.record_error()
            try:
                raise Exception("Expected page title to be: '" + self._page_title + "' but it was: '" + page_title + "'")
            except Exception:
                raise Exception('Expected page title does not match actual page title.')
        else:
            return True

    def click_link(self, link, wait_flag=False,timeout=80000):
        self.selenium.click("link=%s" %(link))
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)
        
    def click(self,locator,wait_flag=False,timeout=80000):
        self.selenium.click(locator)
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)
            
    def type(self,locator, str):
        self.selenium.type(locator, str)
        
    def click_button(self,button,wait_flag=False,timeout=80000):
        self.selenium.click(button)
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)

    def get_url_current_page(self):
        return(self.selenium.get_location())
    
    def is_element_present(self,locator):
        return self.selenium.is_element_present(locator)

    def is_element_visible(self, locator):
        return self.selenium.is_visible(locator)
    
    def is_text_present(self,text):
        return self.selenium.is_text_present(text)
    
    def refresh(self,timeout=80000):
        self.selenium.refresh()
        self.selenium.wait_for_page_to_load(timeout)

    def wait_for_element_present(self, element):
        count = 0
        while not self.is_element_present(element):
            time.sleep(1)
            count += 1
            if count == page_load_timeout/1000:
                self.record_error()
                raise Exception(element + ' has not loaded')

    def wait_for_element_visible(self, element):
        self.wait_for_element_present(element)
        count = 0
        while not self.is_element_visible(element):
            time.sleep(1)
            count += 1
            if count == page_load_timeout/1000:
                self.record_error()
                raise Exception(element + " is not visible")

    def wait_for_element_not_visible(self, element):
        count = 0
        while self.is_element_visible(element):
            time.sleep(1)
            count += 1
            if count == page_load_timeout/1000:
                self.record_error()
                raise Exception(element + " is still visible")

    def wait_for_page(self, url_regex):
        count = 0
        while (re.search(url_regex, self.selenium.get_location(), re.IGNORECASE)) is None:
            time.sleep(1)
            count += 1
            if count == page_load_timeout/1000:
                self.record_error()
                raise Exception("Sites Page has not loaded")

    def record_error(self):
        ''' Records an error. '''

        http_matches = http_regex.match(base_url)
        file_name = http_matches.group(1)

        print '-------------------'
        print 'Error at ' + self.selenium.get_location()
        print 'Page title ' + self.selenium.get_title()
        print '-------------------'
        filename = file_name + '_' + str(time.time()).split('.')[0] + '.png'

        print 'Screenshot of error in file ' + filename
        f = open(filename, 'wb')
        f.write(base64.decodestring(
            self.selenium.capture_entire_page_screenshot_to_string('')))
        f.close()
