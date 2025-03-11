#This script creates a MyRange class that mimics python's built-in range() function

class MyRange:
    def __init__(self,end): #'end' is the upper range input variable
        self.n = 0
        self.end = end

    def __iter__(self): #makes the MyRange class iterable
        return self

    def __next__(self):
        if self.n >= self.end:
            raise StopIteration
        ret = self.n 
        self.n += 1 
        return ret

for x in MyRange(10):
    print(x)
