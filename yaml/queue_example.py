#!/usr/bin/env python
# @author      : ash (nevernew@mail.ru)
# @created     : 14/08/2019
# @description :  

# -*- coding: utf-8 -*-
 
import os
import threading
import certifi
import urllib.request
import urllib3
import json
from queue import Queue
 
 
class Downloader(threading.Thread):
    """Потоковый загрузчик файлов"""
    
    def __init__(self, queue):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        """Запуск потока"""
        while True:
            # Получаем url из очереди
            url = self.queue.get()
            
            # Скачиваем файл
            self.download_file(url)
            
            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()
 
    def download_file(self, url):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
        socket = http.request('GET', url)
        reply = json.loads(socket.data.decode('utf-8'))
        print(reply)
        reply = ''.join(reply)





def main(urls):

    queue = Queue()
    
    # Запускаем потом и очередь
    for i in range(5):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()
    
    # Даем очереди нужные нам ссылки для скачивания
    for url in urls:
        queue.put(url)
 
    # Ждем завершения работы очереди
    queue.join()
 
if __name__ == "__main__":
    urls = [
            "https://query1.finance.yahoo.com/v8/finance/chart/MGNT.ME?range=2d&includePrePost=false&interval=1h&corsDomain=finance.yahoo.com&.tsrc=finance",
            "https://query1.finance.yahoo.com/v8/finance/chart/LKOH.ME?range=2d&includePrePost=false&interval=1h&corsDomain=finance.yahoo.com&.tsrc=finance",
            "https://query1.finance.yahoo.com/v8/finance/chart/YNDX.ME?range=2d&includePrePost=false&interval=1h&corsDomain=finance.yahoo.com&.tsrc=finance",
            "https://query1.finance.yahoo.com/v8/finance/chart/ROSN.ME?range=2d&includePrePost=false&interval=1h&corsDomain=finance.yahoo.com&.tsrc=finance",
            "https://query1.finance.yahoo.com/v8/finance/chart/SBER.ME?range=2d&includePrePost=false&interval=1h&corsDomain=finance.yahoo.com&.tsrc=finance"
            ]
    
main(urls)

