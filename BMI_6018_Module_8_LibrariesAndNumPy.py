#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Carrie Gold
#BMI 6018
#Module 8: Libraries and NumPy

#1. Import numpy as np and print the version number. (5 Points)
import numpy as np
print(np.__version__)


# In[32]:


#2. Create a 1D array of numbers from 0 to 9. Desired output:
#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
my_array = np.array([0,1,2,3,4,5,6,7,8,9])
print(my_array)


# In[53]:


#3. Import a dataset with numbers and texts keeping the text intact in 
#Python Numpy. Use the iris dataset available from 
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
dtype = [('sep_len','f4'),('sep_wid','f4'),('pet_len','f4'),('pet_wid','f4'),('class','U15')]
iris_data = np.genfromtxt(url,delimiter=',',dtype=dtype)
#print(iris_data)


# In[55]:


#4. Find the position of the first occurrence of a value greater than 1.0 
#in petalwidth 4th column of iris dataset. Use the iris dataset available 
#from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
first_occ = np.argmax(iris_data['pet_wid']>1.0)
print("The position of the 1st occurrence of a value greater than 1.0 in petalwidth is",first_occ)


# In[62]:


#5. From the array a, replace all values greater than 30 to 30 and less 
#than 10 to 10.
#Input:
np.random.seed(100)
a = np.random.uniform(1,50,20)
print("Original output:",a)
a[a>30]=30
a[a<10]=10
print("Modified output:",a)

