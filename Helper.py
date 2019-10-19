"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/10/17 20:31
"""
import requests
import re
import logging


def logger(s):
    logging.basicConfig(filename='/Users/mengyuantan/Public/plugin/Logs',
                        format='[%(levelname)s] %(asctime)s %(message)s',
                        filemode="a",
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(s)


def get_fee():
    html = requests.get("http://192.168.168.168")
    pattern = re.compile(r"(?<=fee=')\d*")
    fee = re.findall(pattern, html.text)
    return int(fee[0]) / 1e4


def is_connect():
    url_baidu = "http://www.baidu.com"
    return requests.get(url_baidu).status_code == 200
