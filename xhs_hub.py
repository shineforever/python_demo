# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2018/11/16 15:59'

from selenium import webdriver
import pytest
# import allure
s


@pytest.fixture()
def get_driver():
    # 创建Chrome驱动实例,这里创建driver时，传入chrome_options参数，告诉服务器，我是用移动端浏览器访问的。
    options = webdriver.ChromeOptions()
    options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    # driver = webdriver.Chrome(chrome_options=options)
    ############## 通过Remote调用远程WebDriver ##############
    driver = Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities={
        'platform': 'ANY',
        'browserName': 'chrome',
        'version': '',
        'javascriptEnabled': True
    }, options=options)

    # 设置浏览器大小，让它看起来跟手机的样式差不多。
    driver.set_window_size("380", "680")
    # 设置一个全局的等待超时时间 10s
    driver.implicitly_wait(10)

    driver.get("http://www.youdao.com")
    sleep(5)
    print(driver.title)
    print(driver.current_url)

    yield driver

    driver.quit()



get_driver()
#
#
# @pytest.fixture(scope="session", autouse=True)
# def env():
#     """
#     Parse env config info
#     """
#
#     allure.environment(report="英语移动端官网", browser="Chrome", version="1.0.1")  # 测试报告中展示环境信息
