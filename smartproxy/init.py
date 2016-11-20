# coding=utf-8

from utils import get_cx

__author__ = "ty@puton.info"

def init_db():
    cx = get_cx()
    cu=cx.cursor()
    try:
        cu.execute("create table proxy(id varchar(30) primary key, ip varchar(20), port integer, create_time time)")
        cu.execute("create table proxy_log(id integer primary key autoincrement, proxy_id varchar(30), task_id varchar(30), op_time time)")
    except:
        pass
    cu.close()
    cx.close()