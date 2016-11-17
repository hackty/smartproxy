# coding=utf-8

import time
import sqlite3

__author__ = "ty@puton.info"

def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

def get_cx():
    return sqlite3.connect("smartproxy.db",5000)
