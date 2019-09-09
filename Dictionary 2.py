# For counting the no. of days on which mails are arrived
fh=open('demo.txt')
count=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        w=line.split()
        count[w[2]]=count.get(w[2],0)+1
print('The days on which mails are arrived',count)
print(count.get('Sat')) #Gives the value of the key 'Sat'

fh=open('demo.txt')
c=dict()
largest=0
for line in fh:
    line=line.rstrip()
    if line.startswith('From'):
        mail=line.split()
        id=mail[1]
        c[id]=c.get(id,0)+1
for i in c:
    max=c.get(i)
    if max>largest:
        largest=max
    else:
        continue
for i in c:
    if largest==c.get(i):
        print('{0} {1}'.format(i,largest)) # Printing the email id (key=i) from which has most no. of email sent
print('The email id from which mails are sent :',c) # dictionary

fh=open('demo.txt')
d=dict()
largest=0
for line in fh:
    line=line.rstrip()
    if line.startswith('From'):
        atpos=line.find('@')
        sppos=line.find(' ',atpos)
        l=line[atpos+1:sppos]
        d[l]=d.get(l,0)+1
for i in d:
    max=d.get(i)
    if max>largest:
        largest=max
for i in d:
    if largest==d.get(i):
        print(i, largest) # Maximum no. of Domain names
print(d)


