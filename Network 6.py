import urllib.request,urllib.parse,urllib.error
fh=urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read()
#fh=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
fh=fh.strip()
print('chacters:-',len(fh),'\n')
print(fh[:150].decode())

from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url='http://www.dr-chuck.com/page1.htm'
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
c=0
ta=soup('a')
for tag in ta:
    print('TAG:', tag)
    c=c+1
print(c)

