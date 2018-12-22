# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2018/12/6 19:53'

import requests
from lxml import etree
from fake_useragent import UserAgent
import pymysql

url="https://www.xicidaili.com/nn/"
ua = UserAgent()
headers = {'User-Agent':ua.chrome}

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='!@#QWE',db='article_spider',charset="utf8")
cursor = conn.cursor()

def get_html(url):
    """
    获取指定页面html内容
    :return: 
    """
    try:
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        html = response.text
    except:
        pass

    return html

def get_xici_ips(html):
    """
    获取西刺网免费ip
    :param html: 
    :return: 
    """

    selector = etree.HTML(html)
    trs = selector.xpath('//tr[@class="odd"]')

    ip_list = []
    for td in trs:
        ip = td.xpath('td[2]/text()')[0]
        port = td.xpath('td[3]/text()')[0]
        auth = td.xpath('td[6]/text()')[0]
        speed_str = td.xpath('td[7]/div/@title')[0].split('秒')[0]
        speed = float(speed_str)
        if auth == 'HTTP':
            ip_list.append((ip,port,auth,speed))

    return ip_list

def insert_ips(ip_list):
    """
    插入ip列表
    :param ip_list: 
    :return: 
    """
    for ip_info in ip_list:
        print("insert {0}".format(ip_info[0]))
        try:
            cursor.execute(
                "insert into proxy_ips(ip,port,auth,speed) VALUES('{0}', '{1}', '{2}','{3}')".format(
                ip_info[0], ip_info[1], ip_info[2],ip_info[3]
                )
            )
        except:
            pass
        else:
            conn.commit()

    # conn.close()

if __name__ == '__main__':
    for i in range(2, 200):
        print("start page {0}".format(i))
        url ="https://www.xicidaili.com/nn/{0}".format(i)
        html_text= get_html(url)
        ips = get_xici_ips(html_text)
        print(ips)
        insert_ips(ips)
        print("end page {0}".format(i))

