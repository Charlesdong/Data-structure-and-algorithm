#!/usr/bin/python

import threading
from time import sleep, ctime

loops = [2, 8]
nloops = range(len(loops))
def loop(nloop, nsec):
    print 'start loop',nloop, 'at:',ctime() 
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print "start at:", ctime()
    threads = []

    for i in nloops:
        t = threading.Thread(target = loop, args=(i, loops[i]))
        threads.append(t)

    for i in threads:
        i.start()

    threads[0].join()
    threads[1].join()
    print "all done at:", ctime()

if __name__ == '__main__':
    main()

    print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" 



