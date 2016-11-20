# coding=utf-8

from utils import get_now_time, get_cx

__author__ = "ty@puton.info"

def log_get(proxy_id, task_id):
    cx = get_cx()
    cu=cx.cursor()
    op_time = get_now_time()
    data = (proxy_id, task_id, op_time)
    try:
        cu.execute("insert into proxy_log('proxy_id','task_id','op_time') values (?,?,?)", data)
    except:
        pass
    cx.commit()
    cx.close()
