#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Carrie Gold
#BMI 6030
#Module 5 Advanced Functions and Logic, Part 2

#2. Write the a python program that, given an input list of any level 
#of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with recursion. 
#Note: the input will contain only integers or lists. 

sample_list = [72, 2, 3, 4, [5, 6, 7, [8, 12,[72, 84,[99]]]]]
def in_fun_r(user_input, condition=None):
    if condition is None: 
        try:
            last_element = user_input[-1]
            if isinstance(last_element, list):
                #print("current last element:",last_element)
                in_fun_r(user_input[-1])
            else:
                final_output = [i + 1 for i in user_input]
                print(final_output)
        except:
            condition = 1
in_fun_r(sample_list)


# In[ ]:




