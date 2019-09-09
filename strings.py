num1 = 1.5
num2 = 6.3

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

fruit='banana'
print(fruit)
index=len(fruit)-1
while 0<=index:
    letter=fruit[index]
    print(letter)
    index=index-1
c=0
for char in fruit:
    if char=='a':
        c=c+1
print(c)

n=2.4
m=3.6
print('yes')
sum=n+m
print(sum)

new='j'+fruit[1:4]
print(new)
b=fruit[:]
print(b)

def count(f,l):
    c=0
    for char in f:
       if char==l:
           c=c+1
    return c
string='this is india'
inp=str(input('Enter the word you wanna count...'))
result=count(string,inp)
print(result)

b='a'in fruit
print(b)

# all uppercase letters comes before lowercase letters
word=str(input('enter your word..'))
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

b=type(fruit)
print(b)
c=dir(fruit)
print(c)

a='banana'
c=len(a)-1
b=list()
for i in range(len(a)):
    s=a[c-i]
    b.append(s)
print(b)
h=' '.join(b)
print(h)

