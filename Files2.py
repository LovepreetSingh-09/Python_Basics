fout=open('demo1.txt','w')
print(fout)
line1='This is the place'
fout.write(line1)
fout.write('How good is this')
fout.close()

s='1 2\n3\t4'
print(s)
print(repr(s))

fhand=open(input("Enter the file name.."))
t=0
c=0
for line in fhand:
    line=line.rstrip()
    if 'X-DSPAM-Confidence:' in line:
       print(line)
       atpos=line.find(':')
       n=float(line[atpos+1:])
       print(n)
       c=c+1
       t=t+n
print('Average spam no. is ..',(t/c))


#fhand=open('demo.txt')
for line in fhand:
    print(line.upper())

fname=input('Enter file name...')
try:
    fhand=open(fname)
except:
    if fname=='na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punked')
    else:
        print('File not found',fname)
    exit()
c=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('Subject'):
        print(line)
        c=c+1
print('there are ',c,'subject lines in ',fname)
