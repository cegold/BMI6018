#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Carrie Gold
#BMI 6030
#Module 5 Advanced Functions and Logic, Part 1

#while_inner_plus.py
#1. Write a python program that, given an input list 
# of any level of complexity/nestedness, will return 
#the inner most list plus 1. This is to be done with a 
#while loop. Note: the input will contain only integers or lists. 


# In[119]:


sample_list = [72, 2, 3, 4, [5, 6, 7, [8, 12,[72, 84,[99,[1,2,3]]]]]]
def in_function(user_input, condition = None):
    while condition is None:
        try:
            last_element = user_input[-1]
            if isinstance(last_element, list):
                user_input = user_input[-1]
            else:
                final_output = [i + 1 for i in user_input]
                print(final_output)
                break
        except:
            condition = 1
in_function(sample_list)

