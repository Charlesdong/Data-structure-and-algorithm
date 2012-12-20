#!/usr/bin/python

class A:
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        print 'aaaaaaaaaaaaaaa'
        a = apply(self.func, self.args)

def hello(h):
    print h

if __name__ == '__main__':
    a = A(hello, ('hello world',))
    a()
