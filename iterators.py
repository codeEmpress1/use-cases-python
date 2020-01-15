# Document at least 3 use cases of iterators
# 1. Fibonacci with generator
class MyIterator:
    def __init__(self,num):
        self.num1 = num
        self.first = 0
        self.second = 1
        self.count = 0    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.count > 10:
            raise StopIteration
        else:
            self.first, self.second = self.second, self.first + self.second
            self.count += 1
            return self.second - self.first

# print(list(MyIterator(10)))

# 2.
# Implementing map with iterator

class MyMap:
    def __init__(self, func, iterable):
        self.func = func
        self.iterable = iterable
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
            
            if self.i >= len(self.iterable):
                raise StopIteration
            else:
                mapped = self.func(self.iterable[self.i])
                self.i += 1
                return mapped


# print(list(MyMap(lambda x: x*2, [1,2,3,4,5,6])))


# 3 Implementing a sorting function with generator
class sorter:
    def __init__(self, lst):
        self.lst = lst
        # self.func = func
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.lst):
            raise StopIteration
        else:
            self.i += 1
            return self.lst[self.i]
            # else:
                # self.i += 1
                
print(list(sorter([1,2,3,4,1,1,0,3])))







