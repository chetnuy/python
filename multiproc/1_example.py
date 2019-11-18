#!/usr/bin/env python
# @author      : ash (nevernew@mail.ru)
# @created     : 14/08/2019
# @description : 
import certifi
import urllib3
import json


def foo(ticket):
    link = "https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&fields="
    fields = "symbol,marketState,regularMarketPrice,regularMarketChange,regularMarketChangePercent,preMarketPrice,preMarketChange,preMarketChangePercent,postMarketPrice,postMarketChange,postMarketChangePercent"
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    socket = http.request('GET', link+fields+'&symbols='+ticket)
    reply = json.loads(socket.data.decode('utf-8'))
    return reply

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

for i in range(5):
    async_result = pool.apply_async(foo,('CNY', 'dd')) # tuple of args for foo
    return_val = async_result.get()
    print(return_val)

# do some other stuff in the main process








