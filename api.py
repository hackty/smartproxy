# coding=utf-8

from log import log_get
from utils import dict_factory, get_cx

__author__ = "ty@puton.info"

def get_proxy(task_id):
    cx = get_cx()
    cx.row_factory = dict_factory
    cu=cx.cursor()
    try:
        cu.execute("SELECT * FROM proxy p WHERE p.id NOT IN (SELECT pl.proxy_id FROM proxy_log pl WHERE pl.task_id = '%s')" % (task_id))
        rs = cu.fetchone()
        proxy_id = rs["id"]
        print proxy_id
        cx.close()
        return proxy_id
        # log_get(proxy_id, task_id)
    except:
        pass

def abandon_current_proxy(task_id):
    cx = get_cx()
    cx.row_factory = dict_factory
    cu=cx.cursor()
    try:
        cu.execute("SELECT * FROM proxy p WHERE p.id NOT IN (SELECT pl.proxy_id FROM proxy_log pl WHERE pl.task_id = '%s')" % (task_id))
        rs = cu.fetchone()
        proxy_id = rs["id"]
        print proxy_id
        cx.close()
        log_get(proxy_id, task_id)
    except:
        pass

# get_proxy("dianping")

# abandon_current_proxy("dianping")