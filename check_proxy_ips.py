# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2018/12/19 19:32'


import requests
from fake_useragent import UserAgent
import pymysql

url='http://www.baidu.com'
ua = UserAgent()
headers = {'User-Agent':ua.chrome}

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='!@#QWE',db='article_spider',charset="utf8")
cursor = conn.cursor(pymysql.cursors.SSCursor)

def check_proxy_ip():
    """
    检查ip地址
    :param ip: 
    :return: 
    """
    sql = """
                SELECT ip, port FROM proxy_ips
               """
    #获取所有的ip地址，以后可以修改为分批处理！
    cursor.execute(sql)

    for ip_info in cursor.fetchall():
        ip = ip_info[0]
        port = ip_info[1]
        print("check {0}".format(ip))

        proxies = {
            "http": "http://{0}:{1}".format(ip,port),
        }
        try:
            r = requests.get(url,headers=headers,proxies=proxies,timeout=2)
            r.raise_for_status()
            print('{0} is OK'.format(ip))

        except:
            delete_sql = """
                            delete from proxy_ips where ip='{0}'
                           """.format(ip)
            print("delete {0}".format(ip))
            cursor.execute(delete_sql)
            conn.commit()


    conn.close()


if __name__ == '__main__':
    check_proxy_ip()