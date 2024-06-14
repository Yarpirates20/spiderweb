"""
DESCRIPTION
===========

This module contains a thread class for making web requests.

MODULE CONTENTS
===============

#TODO: write module contents


EXAMPLES
========

#TODO: write examples

"""

import threading
import time
import requests

class WebRequestThread(threading.Thread):
    """ A thread for making web requests. """
    def __init__(self, url) -> None:
        threading.Thread.__init__(self)
        self.url = url
        self.result = f"{self.url}: Custom timeout"

    def run(self):
        res = requests.get(self.url)
        self.result = f'{self.url}: {res.text}'



def processRequests(threads, timeout=5):
    UPDATE_INTERVAL = 0.01
    def aliveCount():
        alive = [1 if thread.is_alive() else 0 for thread in threads]
        return sum(alive)
    
    
    while aliveCount() > 0 and timeout > 0:
        timeout -= UPDATE_INTERVAL
        time.sleep(UPDATE_INTERVAL)
    
    for thread in threads:
        print(thread.result)


def testFunctionMain() -> None:
    urls = [
        'http://httpstat.us/200',
        'http://httpstat.us/200?sleep=4000',
        'http://httpstat.us/200?sleep=20000',   # To check timeout
        'http://httpstat.us/400',
        'http://httpstat.us/404',
        'http://httpstat.us/408',
        'http://httpstat.us/500',
        'http://httpstat.us/524'            
]
    
    start = time.time()

    threads = [WebRequestThread(url) for url in urls]
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
    # for thread in threads:
    #     thread.join()
    # for thread in threads:
    #     print(thread.result)
    processRequests(threads)


    end = time.time()
    print(f'Execution time: {end - start:.2f} seconds')
    print('Done.')





if __name__ == '__main__':
    testFunctionMain()
    
