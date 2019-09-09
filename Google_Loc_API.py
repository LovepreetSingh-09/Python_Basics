import urllib.request,urllib.parse,urllib.error
import ssl
import json

api_key=False

if api_key is False:
    api_key=42
    serviceurl='http://py4e-data.dr-chuck.net/json?'

else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    address=input('Enter location: ')
    if len(address)<1:
        break
    parms=dict()
    parms['address']=address
    if api_key is not False:
        parms['key']=api_key
    url=serviceurl+urllib.parse.urlencode(parms)
    print('Retrieving: ', url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retrieved ',len(data),'Charcters')
    try:
         js=json.loads(data)
    except:
        js=None
    if not js or 'status' not in js or js['status']!='OK':
        print('=====failed to retrieved data=====')
        print(data)
        continue
    print(json.dumps(js,indent=4))
    print(js)
    lat=js['results'][0]['geometry']['location']['lat'] # here {0} can be written as len(c)-1
    Lng=js['results'][0]['geometry']['location']['lng']
    count=(len(js['results'][0]['address_components']))
    c=len(js['results'])
    print(js['results'],'\n',js['results'][0]['address_components'])
    print('Address Components:',count)
    print('Result components:',c)
    loc=js['results'][0]['formatted_address']
    print('Latitude:',lat,'\nLongitude:',Lng,'\nLocation:',loc)
    code=js['results'][0]['address_components'][count-1]['short_name']
    if len(code)==2:
        print('Country Code:',code,'\n')
    else:
        print('===It is not a country===\n')

# The difference between the lengths of the results and the address_components is the no. of curly brackets in that element
gh={'result':[{'ab':'bc','cd':'dc','ef':'fc'}]} # Here the length is 1
mn={'address':[{'ab':'bc'},{'cd':'dc'},{'ef':'fc'}]}  # Here  the length is 3
print(len(gh['result']),len(mn['address']))
print('yes')



