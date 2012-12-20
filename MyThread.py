#!/usr/bin/python

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args=None, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        print "starting", self.name, 'at:', ctime() 
        self.result = apply(self.func, self.args)
        print self.name, 'finished at:', ctime()

    @property
    def get_result(self):
        return self.result

if __name__ == '__main__':
    def test(n):
        print n
        return n

    t = MyThread(test, ('hello',), test.__name__)
    t.start()
    t.join()
    print t.get_result
