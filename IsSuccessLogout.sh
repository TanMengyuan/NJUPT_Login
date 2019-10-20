#!/usr/bin/env bash 

if ping -c 1 -W 1000 www.baidu.com >/dev/null 2>&1
then
	echo Logout failed
else
	echo Successful logout
fi