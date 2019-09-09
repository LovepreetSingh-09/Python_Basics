num1 = 1.5
num2 = 6.3

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
line='sdgbcgjstephen'
print(line.find('stephen'))
fruit='this is india  '
print(fruit.capitalize())
print(fruit.upper())
print(fruit.islower())
print(fruit.find('n')) # gives the index value
print(fruit.find('i',6)) # gives index from the specified number
print(fruit.strip()) # ends the balnk space from starting and ending
print(fruit.startswith('this'))

data='From stephen.marquard@uct,act.za Sat Jan 5 09:14:16 2019'
atpos=data.find('@')
sppos=data.find(' ',atpos)
fdata=data[atpos+1:sppos]
print(fdata)

camels=42 # %d=integers %g=float %s=strings
print('I have seen %d camels' %camels)
print("In %d years I have got %g %s"%(4,8.74,'cgpa'))

# DEBUGGING
while True:
    line = input('> ')
    if line.startswith('#'):  # or Use if len(line)>0 and line[0]=='#'   DON'T USE -> if line[0] == '#':
       continue
    if line == 'done':
       break
    print(line)
print('Done!')

str='X-DSPAM=Confidence:0.8475'
atpos=str.find(':')
no=str[atpos+1:]
print(no)
no=float(no)
print(type(no))


