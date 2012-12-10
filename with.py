#!/usr/bin/python
class controlled_execution(object):
    def __init__(self, filename):
        self.f = None
        self.filename = filename

    def __enter__(self):
        try:
            f = open(self.filename, 'r')
            content = f.read()
            return content
        except IOError, e:
            print "Error %s" % str(e)
    def __exit__(self, type, value, traceback):
        if self.f:
            print "type:%s, value:%s, traceback:%s" % \
                    (str(type)), str(value), str(traceback)
            self.f.close()

def test3():
    with controlled_execution('urllib.py') as thing:
        if thing:
            print 'hello', thing

if __name__ == '__main__':
    test3()
