# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2018/11/16 11:10'


from selenium import webdriver
from pyvirtualdisplay import Display
from time import sleep
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



option = webdriver.ChromeOptions()

# option.add_argument('--headless')
#options.add_argument('--disable-gpu')
# option.add_argument('--no-sandbox')
#option.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
#driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)
# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    desired_capabilities=DesiredCapabilities.CHROME
# )

driver = Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities={
        "start_process" : 'false',
        'platform': 'ANY',
        'browserName': 'chrome',
        'version': '5.3',
        'javascriptEnabled': True
    })
driver.get("http://www.baidu.com")
sleep(5)
print(driver.title)
print(driver.current_url)
driver.get_screenshot_as_file('xhs.png')
driver.delete_all_cookies()
driver.quit()

