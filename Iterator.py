
list=[3,4,8,5]
my_iter=iter(list)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
#print(next(my_iter))    # An error will occur due to the end of the list

class powtwo:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
b=powtwo(3)
print(b.__iter__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

# Another method of using iterator of a class:-
a=powtwo(4)
i=iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# One for method:-
for i in powtwo(5):
    print(i)

# infinite iterator giving 0 every time
int()
inf=iter(int,1)
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))

# Iterator for add numbers:-
class infiter:
    def __iter__(self):
        self.num=-1
        return self
    def __next__(self):
        self.num+=2
        return self.num
b=iter(infiter())
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))