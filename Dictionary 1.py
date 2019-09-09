from sklearn.datasets import load_iris
iris_dataset=load_iris()
print(iris_dataset.keys())
print('The keys of iris datasets:\n{}'.format(iris_dataset.keys()))


gh={'result':[{'ab':'bc','cd':'dc','ef':'fc'}]}
mn={'address':[{'ab':'bc'},{'cd':'dc'},{'ef':'fc'}]}
print(len(gh['result']),len(mn['address']))
print('yes')

eng2pun=dict()
print(eng2pun)
eng2pun['one']='ikk'
print(eng2pun)
eng2pun={'one':'ik','two':'do','three':'ten'}   # The old data removed i.e. one
print(eng2pun)
print(eng2pun['two'])
print(len(eng2pun))
val=list(eng2pun.values())
print('do'in val)
print('do' in eng2pun)    # eng2pun just work for the keys

print(ord('J')) # Converts strings into numbers
from collections import Counter
dtr='here I am at the home'
res=Counter(dtr)
print(res)
print(Counter(dtr))

word='here are we going'
d=dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)

c=dict()
for m in word:
    c[m]=c.get(m,0)+1
print(c)

fh=open('romeo.txt')
count=dict()
for line in fh:
    word=line.split()
    for w in word:
        count[w]=count.get(w,0)+1
print(count)

for k in count:    # k=key
    print(k,count[k])
    if count[k]>1:
        print('\n',k,count[k])

# For displaying keys  alphabetically
counts=dict()
counts={'don':5,'alph':76,'ball':47}
ist=list(counts.keys())
print(ist)
ist.sort()
for k in ist:
    print(k,counts[k])

#  line.translate(str.maketrans(fromstr, tostr, deletestr))    Replace the characters in fromstr with the character in the same position in tostr and delete all characters that are in deletestr.The fromstr and tostr can be empty strings and the deletestr parameter can be omitted.
# import string
# string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# For removing punctuation
import string
fh=open('romeo.txt')
hm=dict()
for line in fh:
    line=line.rstrip()
    line=line.translate(str.maketrans(' ',' ',string.punctuation))
    line=line.lower()
    word=line.split()
    for w in word:
        hm[w]=hm.get(w,0)+1
print(hm)


fh=open('word.txt')
import random
t=['e',3,'fd','ed',5,'rf']
for line in fh:
    line=line.rstrip()
    words=line.split()
    for ele in words:
        eng2pun[ele]=random.choice(t)
s=input('Enter the string key...')
vall=list(eng2pun.keys())
print(eng2pun)
if s in eng2pun and s in vall:
    print(eng2pun[s])
else:
    print('Not found...1')

