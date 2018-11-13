#!/bin/python2

import urllib
from threading import Thread
from Queue import Queue

NUM_WORKERS = 20

class Dnld:
    def __init__(self):
        self.Q = Queue()
        for i in xrange(NUM_WORKERS):
            t = Thread(target=self.worker)
            t.setDaemon(True)
            t.start()

    def worker(self):
        while 1:
            url, Q = self.Q.get()
            try:
                f = urllib.urlopen(url)
                Q.put(('ok', url, f.read()))
                f.close()
            except Exception, e:
                Q.put(('error', url, e))
                try: f.close() # clean up
                except: pass

    def download_urls(self, L):
        Q = Queue() # Create a second queue so the worker
                    # threads can send the data back again
        for url in L:
            # Add the URLs in `L` to be downloaded asynchronously
            self.Q.put((url, Q))

        rtn = []
        for i in xrange(len(L)):
            # Get the data as it arrives, raising
            # any exceptions if they occur
            status, url, data = Q.get()
            if status == 'ok':
                rtn.append((url, data))
            else:
                raise data
        return rtn

inst = Dnld()
for url, data in inst.download_urls(['http://ifconfig.io/ip']*6):
    print url, data
