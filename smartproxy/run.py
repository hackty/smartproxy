# coding=utf-8
from init import init_db

import time
import thread
from proxypool import update_proxy, validate_proxy

__author__ = "ty@puton.info"

init_db()

def update_proxy_service(delay):
    while True:
        print "update_proxy_service start"
        update_proxy()
        time.sleep(delay)

def valid_proxy_service(delay):
    while True:
        print "valid_proxy_service start"
        validate_proxy()
        time.sleep(delay)

def main():
    try:
       thread.start_new_thread(update_proxy_service(120))
       time.sleep(60)
       thread.start_new_thread(valid_proxy_service(600))
    except:
       print "Error: unable to start thread"

main()