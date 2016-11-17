# coding=utf-8

import urllib2

__author__ = "ty@puton.info"

def get_proxy_list():
    req = urllib2.Request('http://api.xicidaili.com/free2016.txt')
    response = urllib2.urlopen(req)
    data = response.readlines()
    proxy_list = []
    for line in data:
        proxy_list.append(line.strip())
    return proxy_list
