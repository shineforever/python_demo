# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2018/11/16 16:55'



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()