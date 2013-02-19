#!/usr/bin/python

import threading 
import datetime

class Threading_class(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print "%s say hello at %s" % (self.getName(), now)


if "__main__" == __name__:
    for i in range(2):
        t = Threading_class()
        t.start()
