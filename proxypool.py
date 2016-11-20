# coding=utf-8

import urllib2
import time
from fetcher import get_proxy_list
from utils import get_now_time, get_cx

__author__ = "ty@puton.info"

req_timeout = 15
testUrl = "http://www.so.com/"
testStr = "search"

def update_proxy():
    proxy_list = get_proxy_list()
    cx = get_cx()
    cu=cx.cursor()
    for line in proxy_list:
        try:
            validate(line)
            full_ip = line.split(':')
            ip = full_ip[0].strip()
            port = full_ip[1].strip()
            create_time = get_now_time()
            data = (line, ip, port, create_time)
            cu.execute("insert into proxy values (?,?,?,?)", data)
            cx.commit()
        except:
            print line, 'error'
    cx.close()

def validate_proxy():
    cx = get_cx()
    cu=cx.cursor()
    cu.execute("SELECT * FROM proxy")
    rs = cu.fetchall()
    for r in rs:
        proxy = r[0]
        try:
            validate(proxy)
        except:
            print proxy, 'expired'
            delete(proxy)
    cx.close()

def delete(proxy):
    cx = get_cx()
    cu=cx.cursor()
    cu.execute("DELETE FROM proxy WHERE id='%s'" % proxy)
    cx.commit()
    cx.close()

def validate(proxy):
    proxyHandler = urllib2.ProxyHandler({'http': '%s' % (proxy)})
    opener = urllib2.build_opener(proxyHandler)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
    t1 = time.time()
    req = opener.open(testUrl, timeout=req_timeout)
    result = req.read()
    timeused = time.time() - t1
    pos = result.find(testStr)
    if pos > 1:
        print proxy, 'valid'
    else:
        print proxy, 'no identification found.'