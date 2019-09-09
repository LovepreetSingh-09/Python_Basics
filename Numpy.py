import numpy as np
list=[5,2,8,9]
arr1=np.array(list,dtype=float)
arr2=np.array(([2,4,2],[5,2,7],[3,3,9]),dtype=int)
print(arr1,'\n',arr2)
arr3=np.array(([2,4,2],[5,2,7],[3,3,9]),dtype=bool)
arr4=np.array(([1,8,'list'],[13,'ba',1]),dtype=object)
print('\n',arr3,'\n',arr4)
print(arr2[1,2])  # 3rd element of the 2nd row
print(arr2[:1,])  # 1st row with every column
print(arr2[:2,:1]) # first 2 rows and 1st column
print(arr2[::-1,]) # reversing the rows such that 1st row becomes the last one and vice-versa
print(arr2[::-1,::-1]) #reversing the rows and columns both such that 1st row and column becomes the last one and vice-versa
print(arr2*2,arr2+2)  # Mathematics operations work on every element of the array
arr2=arr2.astype(float) # Changing the integer array to float
arr2[1,1]=np.nan  # nan(not a number) and inf(infinite) only applies to float
arr2[1,2]=np.inf
print(arr2)
print(arr2.dtype,arr2.shape,arr2.size,arr2.ndim) # Gives the data-type, shape(rows,col),size(no,of elements), dimensions
missing_bool=np.isnan(arr2)|np.isinf(arr2)
arr2[missing_bool]=5  # You can give any number to replace nan and inf
arr2=arr2.astype(int)
print(arr2)
print(arr2.mean(),arr2.min(),arr2.max(),arr2.sum())
print(np.amin(arr2,axis=0))  # Gives the array of minimum numbers column-wise
print(np.amin(arr2,axis=1))  # Gives the array of minimum numbers row-wise
# axis=0 means columns and axis=1 means rows
print(np.amax(arr2,axis=0))
print(np.cumsum(arr2)) # It gives a 1 dimensional array of cummulative sum which means addition of last element to every next element
arr=arr2[:2,:2]
print(arr)
arr[1,1]=100 # change to an array which is made from another array causes the change in its parental array
print(arr2)
# To stop the change in the parental array use the copy command
arr=arr2[:2,:2].copy()
print(arr)
arr[0,1]=101
print(arr2)
ar=np.array(([2,3,7],[3,6,1],[4,3,2],[5,1,8]),dtype=int)
print(ar)
print('New array ',ar.reshape(2,6)) # Reshape converts the array into desired no. of rows and columns but the size should be the same
print(ar.ravel())
b=ar.ravel()  # ravel also converts the array into one dim array and any change in the child array of it can cause the same change in the parental arrat
b[0]=100
print(ar)
print(ar.flatten()) # converts the array into one dimensional array but any change in the child array of it will not cause any change in the parental a
b=ar.flatten()
b[6]=100
print(ar)
l=ar.tolist()
print(l)
print(np.eye(3,3))
print(np.eye(3,3,dtype=int))
print(np.ones((3,4),dtype=int))
print(np.zeros((3,4)))
print(np.zeros((3,4),dtype=int))
print(np.arange(5))
print(np.arange(1,24,2))
print(np.arange(10,2,-2)) # 1st=start ,2nd=end, 3rd=steps
p=np.linspace(start=1,stop=50,num=9,dtype=int) # number indicates how many numbers between start and stop
print(p)
np.set_printoptions(precision=2)  # Means values upto 2 decimal points
n=np.logspace(start=1,stop=10,num=5,base=10)
print(n)
# The difference between the tile and repeat is that tile repeats the whole list while repeat repeats every element of the list
a=[1,2,3]
print('Tile:',np.tile(a,2))
print('Repeat:',np.repeat(a,2))
print(np.random.rand(3,2)) # Random numbers between 0 and 1 of shape(3,2)
print(np.random.randn(3,2)) # Random numbers having normal distribution with mean=0 and variance=1 of shape(3,2) Basically a curve of mean 0
help(np.random.randn)
print(np.random.randint(5,50,size=(4,3)))
print(np.random.random()) # One random number between 0 and 1
print(np.random.random(size=(2,2)))
print(np.random.choice(['aa','f','v','r','e'],size=10)) #Gives 10 random elements having equal probability of every element
print(np.random.choice(['a','e','i','o','u'],size=10,p=[0.3,0.2,0.1,0.1,0.3])) # Gives 10 random elements where every element has some probability and sum of all probabilities should be 1
rn=np.random.RandomState(100)
print(rn.rand(2,2))
# by this the random numbers produced by setting a randomstate or random seed will be the same
np.random.seed(100)
print(np.random.rand(2,2))
# Here we get all the unique no. and the count that how many times did they come in the array
np.random.seed(100)
a=np.random.randint(0,10,size=10)
print(a)
uniqs,counts=np.unique(a,return_counts=True)
print('Unique items:',uniqs)
print('Counts\t\t:',counts)
# Getting index location
arr=np.array(([3,6,2],[4,4,8],[1,4,3]),dtype=int)
print(arr,'\n',np.where(arr>4))
i=np.where(arr>4)
print(arr.take(i)) # Gives values only for the 1D array
print(arr[i]) # Gives values for nD arrays
print(np.where(arr>4,'m','n'))
print(np.argmin(arr)) # Gives value of 2D array in a single number starting from 0
print(np.argmax(arr))
# Turn On scientific notation
np.set_printoptions(suppress=True)
path='https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv'
data=np.genfromtxt(path,delimiter=',',skip_header=1,filling_values=25,dtype=int)
print(data)
np.savetxt('csv1.csv',data,delimiter=',')

np.set_printoptions(suppress=True)
path='https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv'
data=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=object) # We can use NONE in place of object
print(data)
a=np.random.rand(1,3)
print(a)
# for applying these 3 methods the size and shape of both the arrays should be same
am=np.array(([1,2,6],[1,6,1],[8,2,7]),dtype=int)
print(np.concatenate([arr,am],axis=0))
print(np.hstack([arr,am]))  # hstack = for merging column-wise // vstack= for merging row-wise
print(np.c_[arr,am])  # np.c_=column add   //  np.r_=rows add
# axis=1 for sorting rows and axis=0 for sorting columns and by this method all the elements will be sorted
print(arr,np.sort(arr,axis=1))
print(arr,np.sort(arr,axis=0))
print(np.where(arr==am[0][:50]))