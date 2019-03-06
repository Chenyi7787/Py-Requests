#!/usr/bin/env python3
# -*- coding:utf-8 -*-



import requests



if __name__=="__main__":

	r=requests.get("https://api.github.com/events")

	print(r.text)
