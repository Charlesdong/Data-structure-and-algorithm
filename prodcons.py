#coding=utf-8
#!/usr/bin/python
#生产者消费者问题

from MyThread import MyThread
from random import randint
from time import sleep
from Queue import Queue

def writeQ(queue):
    print "product a object for Q ..."
    queue.put('xxx', timeout=1)
    print "product done", queue.qsize()

def readQ(queue):
    print "get a object from Q ..."
    result = queue.get(timeout=1)
    print "get done", queue.qsize()

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
    sleep(randint(1,3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
    sleep(randint(2,5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), name=funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print "all done"

if __name__ == '__main__':
    main()
    print 'Thank you !'
