import re
fh=open('demo1.txt')
for line in fh:
    line=line.rstrip()
    if re.search('^F..m.+@',line):
        print(line)

fh=open('demo1.txt')
for line in fh:
    line=line.rstrip()
    x=re.findall('\S+@\S+',line)
    if len(x)>0:
        print(x)

print('\n')
fh=open('demo1.txt')
for line in fh:
    line=line.rstrip()
    x=re.findall('[A-Za-z0-9]+@[.a-zA-Z]+',line)
    if len(x)>0:
        print(x)

print('\n')
fh=open('demo1.txt')
for line in fh:
    line=line.rstrip()
    x=re.findall('^X\S*: ([0-9.]+)',line)
    if len(x)>0:
        for i in x:
            print(i)

print('\n')
fh=open('demo1.txt')
for line in fh:
    line=line.rstrip()
    m=re.findall('^Details:.*rev=([0-9.]+)',line)
    if len(m)>0:
        print(m)


print('\n')
fh=open('demo1.txt')
for line in fh:
    line=line.rstrip()
    gh=re.findall('^From .* ([0-9][0-9]):',line) # space before [] shows that there should be no character before the hour
    if len(gh)>0:
        print(gh)

# \$ or \. or \+ or \* or \? represent this special character is in the string
x='We just received the $10.00 for cookies'
m=re.findall('\$[0-9.]+',x)
print(m)


print('\n')
c=0
t=0
fh=open('demo.txt')
for line in fh:
    line=line.rstrip()
    x=re.findall('New Revision: ([0-9.]+)',line)
    if len(x)>0:
        for i in x:
            c=c+1
            f=int(i) # converting string into integer
            t=t+f
avg=t/c
print(avg,'\n',t,c)

