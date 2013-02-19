
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

def second_test(aList):
    """O(N^2)"""
    n = len(aList)
    MaxSum = 0
    for i in range(0, n):
        ThisSum = 0
        for j in range(i, n):
            ThisSum += aList[j]
            if ThisMax > MaxSum: 
                MaxSum = ThisMax
    return MaxSum

if __name__ == '__main__':
    aList = [-9, 10, -3]
    #result = first_test(aList)
    result = first_test(aList)
    print "result is: ", result

