#!/usr/bin/python

def Feb(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b 
        n = n + 1

f = Feb(5)
f.next()
