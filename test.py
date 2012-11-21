#!/usr/bin/python

def first_test(aList):
    """Just for max sub list O(N^3)"""
    n = len(aList)
    MaxSum = 0
    for i in range(0, n):
        for j in range(i+1, n):
            ThisMax = 0
            for k in range(i, j+1):
                ThisMax += aList[k]
            
            if ThisMax > MaxSum:
                MaxSum = ThisMax
    return MaxSum

if __name__ == '__main__':
    aList = [0, 31, -2, 4, -4]
    result = first_test(aList)
    print "result is: ", result

