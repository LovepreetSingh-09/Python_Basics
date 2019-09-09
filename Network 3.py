import urllib.request,urllib.parse,urllib.error
img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fh=open('cover2.jpg','wb')
s=0
while True:
    info=img.read(100000)
    if len(info)<1:
        break
    s=s+len(info)
    fh.write(info)
print(s,"Characters copied")
fh.close()



