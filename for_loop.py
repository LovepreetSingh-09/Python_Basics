def jpeg(filename):
    with open (filename,'rb') as fh:
        print(fh.seek(163))
        a=fh.read(2)
        print(a[0],a[1])
        height=(a[0] << 8)+a[1]
        a=fh.read(2)
        print(a[0],a[1])
        width=(a[0]<<8)+a[1]
        print('Resolution is :',height,"*",width )
jpeg('cover2.jpg')

friends=['jake','smith','steve']
for m in friends:
    print('Happy Diwali..',m)
print('Done..!')

total=0
for i in [2,54,24,15,16,15]:
    total=total+i
print(total)

small=None
print('smallesst..', small)
for i in [2,4,1,5,8,9]:
    if small is None or i<small:
        small=i
    print(small, i)
print('smallest...', small)

t=0
c=0
while True:
    inp=input('Enter the no....')
    if inp=='done':
        break
    try:
        n=float(inp)
        c=c+1
        t=t+n
    except:    
        print('Invalid Input !')
avg=t/c
print('Count...',c,'\nTotal...',t,'\nAverage....',avg)

