from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url='http://www.dr-chuck.com/page1.htm'
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
for tag in tags:
    print('TAG:',tag)
    print('\n\n\nURL:',tag.get('href',None))
    print('\nContents:',tag.contents[0])
    print('Attrs:',tag.attrs)
