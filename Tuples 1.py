t=('a','b',1,'d',9)
print(type(t))
t=tuple()
print(t)
t=tuple('hello')
print(t)
print(t[1])
print(t[1:3])
t=('A',)+t[1:] # single tuple element comes up with a comma after it
print(t)
f=(0,5,8)>(4,3,5)
print(f)

txt='but soft what light in younger window breaks'
words=txt.split()
l=list()
for w in words:
    l.append((len(w),w))
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
res=list()
for length,word in l:
    res.append(word)
print(res)

m=['have','fun']
(x,y)=m
j=(x,y)
print(x,y)
print(type(j)) # j is tuple

d={'a':5,'d':7,'b':4}
t=d.items()
print(t,type(t),type(d))
h=list(t)
print(h)
h.sort() # sort first elements
print(h)
h.sort(reverse=True)
print(h)
l=list()
for key,value in list(d.items()):
    print(value,key)
    l.append((value,key))
print(l)
l.sort()
print(l)

g=d.items()
print(g)

import string
fh=open('word.txt')
count=dict()
for line in fh:
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.lower()
    word=line.split()
    for w in word:
        count[w]=count.get(w,0)+1
lst=list()
for key,val in list(count.items()):
    lst.append((val,key))
lst.sort(reverse=True)
for k,va in lst[:10]:
    print(k, va)



