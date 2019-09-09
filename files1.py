import graphviz
import mglearn
mglearn.plots.plot_animal_tree
import os
print(os.getcwd())
#print(os.getcwdb())   #this gives the directory in bytes object
# os.chdir()  # for changing directory enter thr name of directory in the brackets
os.listdir() # all the subdirectories or files in it will be shown in a list
# os.mkdir()  # for making new directory enter thr name of directory in the brackets
#os.rename('current_name','New_name') # for renaming a directory or a file name
#os.remove() # for removing the directory or a file enter thr name of directory in the brackets
#os.rmdir()  # for removing empty directories
import mglearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from sklearn.model_selection import train_test_split

# Binary Classification :-

# ? = w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b > 0
# If the function is smaller than zero, we predict the class ?1; if it is larger than zero, we predict the class +1.
# The two most common linear classification algorithms are 1.) logistic regression, implemented in linear_model.LogisticRegression ; Despite its Regression in name It is a classification algorithm
# 2.) linear support vector machines (linear SVMs), implemented in svm.LinearSVC (SVC stands for support vector classifier)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
X,y=mglearn.datasets.make_forge()
#X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42)
fig,axes=plt.subplots(1,2,figsize=(10,5))
for model,ax in zip([LinearSVC(),LogisticRegression()],axes):
    clf=model.fit(X,y)
    mglearn.plots.plot_2d_separator(clf,X,fill=False,eps=0.5,alpha=0.8,ax=ax)
    mglearn.discrete_scatter(X[:,0],X[:,1],y,ax=ax)
    # Below always use double underscore
    ax.set_title('{}'.format(clf.__class__.__name__))
    ax.set_xlabel('Feature 0')
axes[0].set_ylabel('Feature 1')
axes[0].legend()
plt.show()

hr=45
rate=15
pay=hr*rate
print('the pay is...',pay)

fhand=open('demo.txt')
c=0
l=0
for line in fhand:
    c=c+1
    l=l+len(line)
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)
    if not line.startswith('From'):
        continue
print('lines count is...%d \nlength is ....%d'%( c,l))

#fhand.close() FOR CLOSING

# OR USE this (ONLY ONE OF THESE CAN BE USED)

#(fh=open('demo.txt')
#inp=fh.read()
#print(len(inp))
fhand=open('demo.txt')
for line in fhand:
    line=line.rstrip()
    if line.find('@uct.ac.za')==-1:
        continue
    print(line)

fhand=open('demo.txt')
for line in fhand:
    line=line.rstrip()
    if line.find('stephen')==-1: # find() returns the position or -1(if string not found)
        continue
    print(line)
