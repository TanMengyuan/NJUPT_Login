#!/usr/bin/env bash 

if  ping -w 1 www.baidu.com >/dev/null 2>&1
then
	echo Logout failed
else
	echo Successful logout
fi