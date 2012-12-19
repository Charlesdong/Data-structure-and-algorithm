class Time60(object):
    def __init__(self, hr, min):
        assert isinstance(hr, int), 'must input a number !'
        assert isinstance(min, int), 'must input a number !'
        
        self.hr = hr
        self.min = min

    def __str__(self):
        return str(self.__class__) + '%d : %d' % (self.hr, self.min)

    def __add__(self, other):
        return self.__class__(self.hr+other.hr, self.min+other.min) 

    def __iadd__(self, other):
        ''' suppert like +=, but must return self'''
        self.hr += other.hr
        self.min += other.min
        return self

if __name__ == '__main__':
    a = Time60(23, 3)
    b = Time60(1, 2)

    print a
    print b
    print a+b
    a += b
    print a
