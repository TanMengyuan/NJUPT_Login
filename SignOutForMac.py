"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/10/17 20:31
"""
import requests
from Helper import get_fee, logger


if __name__ == "__main__":
    try:
        fee = get_fee()
        url = "http://192.168.168.168/F.htm"
        requests.get(url=url)
        logger("NJUPT has sign out.")
        logger("余额 Balance: %.2f RMB" % fee)
        print("余额 Balance: %.2f RMB" % fee)
    except:
        logger("Connection Failed.")
        print("Connection Failed.")
