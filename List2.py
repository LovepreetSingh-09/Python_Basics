v="hlo1"
t=list(v)   # list is a command to make element of every letter
print(t)
h='There is a better laptop'
l=h.split() # split makes element of every word
print(l)
print(l[2])
s='I,am,a,good,man'
delimiter=','
print(s.split(delimiter))
print(s.split('-'))
com=' '
print(com.join(h))

fhand=open('demo.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        #print(words[2])
        for wor in words:
            if '@'in wor:
                print(wor)
            #if wor.find('@')==-1:
             #   continue
            #else:
             #   print(wor)

a=[1,2,3]
b=[1,2,3]
print(a is b) # Because a & b are equivalent but not identical (value is same but objects are different)
print(a is [1,2,3]) # This is also false
c=a
print(a is c) # True because both are identical
c[1]=5
print(a) # Change will occur to both the objects

def delete_head(t):
    del t[0]
letter=['a',2,'3']
delete_head(letter)
print(letter)

t1=[1,2]
t2=t1.append(3) # Append modifies the list and does'nt return the value
print(t1,'\n',t2)

t2=t1+[3] # + creates new list and obviously returns value
print(t2)

def tail(t):
    return t[1:]
rest=tail(t1)
print(rest)

def chop(s):
    del s[0]
    del s[-1]
def middle(s):
    s=s[1:]
    s=s[:-1]
    return s
li=[1,2,3,4,5]
ni=[1,2,3,4,5]
one=chop(li)
new=middle(ni)  # li modifies, one is none, ni does'nt changes and new will get modified values
print(li,'\n',one,'\n',ni,'\n',new)

t=['b','c','a','d']
orig=t[:]
t.sort()
print(orig,'\n',t)

fh=open('romeo.txt')
ist=[]
for line in fh:
    word=line.rstrip()
    ele=line.split()
    for element in ele:
        if element not in ist:
            ist.append(element)
        else:
            print('Already there..')
ist.sort()
print(ist)

fh=open('demo.txt')
c=0
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        c=c+1
        line=line.split()
        print(line[1])
    else:
        continue
print(c)

lis=[]
c=0
t=0
while True:
    s=input('Enter the number...')
    try:
        f=float(s)
        c=c+1
        t=t+f
        lis.append(f)
    except:
        if s=='done':
            break
        else:
            print('Invalid input')
print(max(lis),'\n',min(lis))

