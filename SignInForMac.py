"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/10/17 20:31
"""
import getopt
import json
import sys

import requests

from Helper import get_fee, is_connect, logger

CONFIG_FILE = '/Users/mengyuantan/Public/plugin/config.json'

with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
    config = json.load(f)
    username = config["username"]
    password = config["password"]
    key = config["0MKKey"]

url_njupt = "http://192.168.168.168/0.htm"
data = {"DDDDD": username, "upass": password, "0MKKey": key}

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "o")
    is_logout = False
    for op, value in opts:
        if op == "-o":
            is_logout = True

    try:
        requests.post(url=url_njupt, data=data)
        if not is_logout:
            if is_connect():
                fee = get_fee()
                logger("NJUPT has sign in.")
                logger("余额 Balance: %.2f RMB" % fee)
                print("余额 Balance: %.2f RMB" % fee)
            else:
                logger("Connection Failed.")
                print("Connection Failed.")
    except:
        logger("Connection Failed.")
        print("Connection Failed.")
