# smartproxy
yet another auto proxy provider

## installation
pip install smartproxy

## usage(proxy hunter)
>
./smartproxy

## usage(proxy provider)
>
from smartproxy.api import *  
proxy = get_proxy(your_task_id)  
abandon_current_proxy(your_task_id)  

