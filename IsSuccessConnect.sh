#!/usr/bin/env bash 

if ping -c 1 -W 1000 www.baidu.com >/dev/null 2>&1
then
	echo Successful login
else
	echo Login failed
fi