#!/usr/bin/env bash 

/usr/local/Cellar/python/3.7.4/bin/python3 /Users/mengyuantan/Public/plugin/SignInForMac.py -o
msg=$(/usr/local/Cellar/python/3.7.4/bin/python3 /Users/mengyuantan/Public/plugin/SignOutForMac.py)
echo "$msg"
