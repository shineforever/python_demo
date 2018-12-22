# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2018/12/1 18:20'


import requests

url="http://web.http.cnapi.cc/index/index/get_my_balance?neek=55787&appkey=79c0afb4c7a95dd34c9fe3aad6460720"
r = requests.get(url)

if r.status_code == requests.codes.ok:
    result = r.json()
    # print(result)
    balance = result['data']['balance']

    if float(balance) > 50:
        print("ok")


