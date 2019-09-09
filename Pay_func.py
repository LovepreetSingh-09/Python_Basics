hr=int(input('Enter hours...'))
rate=int(input('Enter rate...'))
def computepay(h,r):
    pay=h*r
    if(h>40):
        p=(r/2)*(h-40)
        pay=pay+p

    return pay

fp=computepay(hr,rate)
print('The pay is...',fp)




        
        
