# -*- coding:utf-8 -*-
from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pyperclip
import unittest

url_clipboard = "https://clipboardjs.com/"
url_google = "https://google.com/"
locator_copy = ".input-group-button"
locator_get_text = "id('foo')"
search = "lst-ib"


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def test_get_clipboard(self):
        self.driver.get(url_clipboard)
        self.driver.find_element_by_css_selector(locator_copy).click()
        text_clipboard = Tk().clipboard_get()
        text = self.driver.find_element_by_xpath(locator_get_text).get_attribute("value")
        assert (text_clipboard == text)

    def test_past_clipboard(self):
        self.driver.get(url_google )
        self.driver.find_element_by_id(search).click()
        pyperclip.copy("Hello world!")
        self.driver.find_element_by_id(search).send_keys(Keys.COMMAND + 'v')
        text = self.driver.find_element_by_id(search).get_attribute("value")
        text_clipboard = Tk().clipboard_get()
        assert (text_clipboard == text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()