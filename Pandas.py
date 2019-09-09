import numpy as np
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
print(pd.DataFrame(data,index=['one','two','three'],columns=['Name','Age'],dtype=float))
# in lists we can give the name of the columns but in ductionaries keys are the columns
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
print(pd.DataFrame(data,index=['r','c',3,5]))
print(pd.DataFrame(data,index=['r','c',3,5],columns=['Name']))  # we can use the key in columns section to get the info of only that key
# We can use the index command inside the dictionary
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
print(pd.DataFrame(d))
df=pd.DataFrame(d)
# pd.Series is a command which can be used inside the dictionary to give values and index to the keys
print(pd.Series([1,3,5,7]))
print(df['one']) # keys can also be used to get the information of that column because keys act as columns
df['three']=pd.Series([3,5,7,2],index=['a','b','c','d']) # To add a column as a key to the dataframe we must give the index to every element
print(df)
# We can also add 2 columns or keys to make a new column or a key
df['four']=df['one']+df['three']
print(df) # Similarly we can use +,-,/,* or any other logical operation to make a new column or key
# Deletion of a column or a key can be done by using by del or pop command
del df['four']
print(df)
df.pop('three')
print(df)
# Finding a specific row or index by using the index name
print(df.loc['b'])
# Finding a specific row by using the number of that row
print(df.iloc[2])
# slicing can also be done in pandas but everytime we need to use colon in square brackets
print(df[2:4])
# addition of a dataframe into other dataframe can also be done
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df=df.append(df2) # Addition can be done by using append command
print(df)
# deletion of a specific row can be done by using drop command
df=df.drop(0)
print(df)
# pandas.Panel is used for the multidimensional data more than 2 dimensions
# Representation:-  pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
# item= axis=0
# major axis=1
# minor axis=2
data=np.random.rand(2,3,2)
print(data,'\n',pd.Panel(data))
# We can also make the panel of 2 dataframes
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
print(data,'\n',pd.Panel(data))
# finding data using the item or axis=0
p=pd.Panel(data)
print(p['Item1'])
# Finding data using major axis axis=1
print(p.major_xs(1))  # We need to give the column number
# Finding data using minor axis
print(p.minor_xs(2))
# we make an object s using pd.series
s = pd.Series(np.random.randn(4))
print(s,'\n',s.axes) # axes = returns the list of row indexes
print(s.empty)  # whether the object is empty or not
print(s.ndim)
print(s.size)
print(s.values) # Gives list of values
print(s.head(3))  # head gives the values from the upper side
print(s.tail(2))  # tail gives the values from the bottom side
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df=pd.DataFrame(d)
print(df)
print(df.T) # Gives the transpose of the dataframe
print(df.axes)
print(df.dtypes)
print(df.empty)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.values)
print(df.head(4))
print(df.tail(3))
print(df.sum()) # Gives the sum of every element of a column
print(df.sum(1)) # Gives the sum of the rows of the columns from a specified column , here it is 1 so, sum of every element of column 1 with that of column 2
print(df.mean())
print(df.std())
print(df.describe()) # Gives summary of the numerical columns
# () and (include='number') gives summary of numerical columns , (include=object) for strings , (include='all]) for all
print(df.describe(include=object))
print(df.describe(include='all'))
print(df.describe(include='number'))
print(df.plot.bar())
def adder(e,r):
    return e+r
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
(df.pipe(adder,2))
print(df.apply(np.mean))

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df,'\n',df.apply(np.mean)) # The mean is performed row-wise by default
print(df.apply(np.mean,axis=1)) # Now the mean is performed column-wise
df=df.apply(lambda x: x.max()-x.min())
print(df.apply(np.mean),'\n',df)
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df['col1']=df['col1'].map(lambda x: x*100)
print(df,'\n',df.apply(np.mean))
