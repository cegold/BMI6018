#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Carrie Gold
#BMI 6030
#Module 5 Advanced Functions and Logic, Part 3

#3.    Write a python program that, given an input list, 
#will filter the input above a user-defined threshold. 
#This is to be done with a standard function.

#That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), 
#it should return [1,2,3,4,5,6].

example_list = [0,22,7,1,2,3,4,5,6]
def cut_off(input_list, n):
    new_list = []
    for i in input_list:
        if i == n:
            new_list.append(i)
            break
        else:
            new_list.append(i)
    print(new_list)
        
cut_off(example_list, 7)


# In[ ]:




