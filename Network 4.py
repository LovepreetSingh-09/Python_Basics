import  urllib.request,urllib.parse,urllib.error
import ssl
import re
# Ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url='https://docs.python.org'
html=urllib.request.urlopen(url).read()
links=re.findall(b'href="(http[s]?://.*?)"',html)
for link in links:
    print(link.decode())

print('\n\n\n\n')
from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url='https://docs.python.org'
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
# Retrieve all of the anchor tags
tags=soup('p')
for tag in tags:
    print('\n\nTAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
