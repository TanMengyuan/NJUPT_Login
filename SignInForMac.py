"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/10/17 20:31
"""
import requests
import json
from Helper import get_fee, is_connect

CONFIG_FILE = '/Users/mengyuantan/Public/plugin/config.json'

with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
    config = json.load(f)
    username = config["username"]
    password = config["password"]
    key = config["0MKKey"]

url_njupt = "http://192.168.168.168/0.htm"
data = {"DDDDD": username, "upass": password, "0MKKey": key}

if __name__ == "__main__":
    try:
        requests.post(url=url_njupt, data=data)
        if is_connect():
            fee = get_fee()
            with open("/Users/mengyuantan/Public/plugin/tmp", "w+") as f:
                f.write("余额 Balance: %.2f RMB" % fee)
        else:
            with open("/Users/mengyuantan/Public/plugin/tmp", "w+") as f:
                f.write("Connection Failed.")
    except:
        with open("/Users/mengyuantan/Public/plugin/tmp", "w+") as f:
            f.write("Connection Failed.")
