#!/usr/bin/python

def isequal(line, key):
    l = line.split()
    for i,value in enumerate(l):
        if i != 1 and value == key:
            l.remove(value)
    return ' '.join(l)
            
    
with open("aaa.txt", "r") as f:
    lines = f.readlines()

    new_lines = map(isequal, lines, [key.split()[1] for key in lines])

with open('aaa.txt', "w") as f:
    f.writelines('\n'.join(new_lines))
