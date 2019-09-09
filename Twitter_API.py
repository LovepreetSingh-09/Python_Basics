import urllib.request,urllib.parse,urllib.error
import ssl
import oauth
import hidden
import twitter1
import json
import twurl
twitter_url='https://api.twitter.com/1.1/statuses/user_timeline.json'
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
while True:
    print(' ')
    acct=input('Enter twitter account....')
    if len(acct)<1:
        break
    url=twurl.augment(twitter_url,{'screen_name':acct,'count':'2'})
    print('Retrieving',url)
    connection=urllib.request.urlopen(url,context=ctx)
    data=connection.read().decode()
    print(data[:250])
    headers=dict(connection.getheaders())
    print('Remaining:',headers['x-rate-limit-remaining'])
