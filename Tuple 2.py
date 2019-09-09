fh=open('demo.txt')
d=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From'):
        word=line.split()
        w=word[1]
        d[w]=d.get(w,0)+1
r=list()
for h,j in list(d.items()):
    r.append((j,h))
print(r)
r.sort(reverse=True)
for k,v in r[:2]:
    print(v,k)

fh=open('demo.txt')
count=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        atpos=line.find(':')
        hr=line[atpos-2:atpos]
        count[hr]=count.get(hr,0)+1
g=list()
for k,v in list(count.items()):
    g.append((k,v))
g.sort()
for k,v in g:
    print(k,v)

fh=open('demo.txt')
h=dict()
for line in fh:
    line=line.strip()
    line=line.lower()
    for w in line:
        if ord(w)>=97 and ord(w)<=122:
            h[w]=h.get(w,0)+1
f=list()
print(h)
for k,v in list(h.items()):
    f.append((v,k))
f.sort(reverse=True)
for v,k in f:
    print(k,v)
