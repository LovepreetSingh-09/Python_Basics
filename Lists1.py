numbers=[5,23,13,4,7,3,15]
print(range(len(numbers)))
for i in range(len(numbers)):
    numbers[i]=numbers[i]*2
    print(numbers[i])
print(numbers)

for i in numbers:
    print(i)

empty=[]
for x in empty:
    print('This never happens')  # the body will never executes in empty listo

listo=['hlo',3,3.5,[9,'rutherford']]
print(listo)

a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*3)
print(listo[1:5])
print(listo[:])
listo[1:3]=['hi',5]
print(listo)
listo.append(a) # Append Make a nested listo in the listo itself and returns no value
print(listo)
print(listo[3])
listo.extend(b) # Extend makes new elements in the listo and returns no value
print(listo)
l=['b','d','a','b']
l.sort() # sort does'nt returns values
print(l)
x=listo.pop(3) # Deletes the 3rd index from listo
print(listo,'\n',x)
y=listo.pop() # Deletes the last index value
print(listo,'\n',y)
del listo[3] # Same as last but don't return the value
print(listo)

print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sum(numbers))

print(sum(numbers)/len(numbers))

listo=[]
while True:
    n=input("Enter a number.....")
    try:
        value=float(n)
        listo.append(value)
    except:
        if n=='done':
            break
        else:
            print("Wrong value")
print(listo)
print(sum(listo)/len(listo))

fh = open('romeo.txt')
ist = list()
for line in fh:
    word = line.rstrip()
    ele = line.split()
    for element in ele:
        if element not in ist:
            ist.append(element)

ist.sort()
print(ist)
