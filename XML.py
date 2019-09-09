import xml.etree.ElementTree as ET
data='''
<person>
  <name>chuck</name>
  <phone type="intl">
   +919779720767
   </phone>
   <email hide="yes"/>
   </person>'''
tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))

import xml.etree.ElementTree as ET
input='''
<stuff>
<users>
  <user x="2">
  <id>11607519 </id>
  <name>Chuck</name>
 </user>
   <user x="7">
   <id>"1609100" </id>
   <name>Brent</name>
  </user></users>
  </stuff> '''
stuff=ET.fromstring(input)
list=stuff.findall('users/user') # if we use(stuff.findall('user') the user count or len(list) will be 0 because everytime we need the top node other than the parent
print('User Count:',len(list))
print(list) # [<Element 'user' at 0x00000292DA7524F8>, <Element 'user' at 0x00000292DA7525E8>] gives this output
for m in list:
    print('\n\nName:',m.find('name').text)
    print('Id:',m.find('id').text)
    print('Attribute:',m.get('x')) # find() gives the value of an element while get() gives the value of element with = sign

# JSON
import json
data = '''
[
{ "id" : "001",
"x" : "2",
"name" : "Chuck" } ,
{ "id" : "009",
"x" : "7",
"name" : "Brent"
} ] '''
stuff=json.loads(data) # stuff is the list having dictionaries of two users
print(stuff,'\nCount:',len(stuff))
for k in stuff:
    print(k)
    print('\nName:',k['name'])
    print('Id:',k['id'])
    print('Attr:',k['x'])

    