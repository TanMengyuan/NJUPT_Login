#!/usr/bin/env bash 

/usr/local/Cellar/python/3.7.4/bin/python3 /Users/mengyuantan/Public/plugin/SignInForMac.py
echo "[INFO] NJUPT had sign in at: $(date "+%Y-%m-%d %H：%M：%S")" >> /Users/mengyuantan/Public/plugin/Logs
echo $(cat /Users/mengyuantan/Public/plugin/tmp) >> /Users/mengyuantan/Public/plugin/Logs