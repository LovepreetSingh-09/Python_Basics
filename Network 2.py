import urllib.request, urllib.parse, urllib.error
fh=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fh:
    print(line.decode().strip())

import urllib.request, urllib.parse,urllib.error
fh=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count=dict()
for line in fh:
    word=line.decode().split()
    for w in word:
        count[w]=count.get(w,0)+1
print(count)

img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fh=open('cover3.jpg','wb')
fh.write(img)
fh.close()
