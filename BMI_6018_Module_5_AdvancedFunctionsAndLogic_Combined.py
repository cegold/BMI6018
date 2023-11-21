#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Carrie Gold
#Module 5: Advanced Functions and Logic

#while_inner_plus.py
#1. Write a python program that, given an input list 
# of any level of complexity/nestedness, will return 
#the inner most list plus 1. This is to be done with a 
#while loop. Note: the input will contain only integers or lists. 


# In[ ]:


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


# In[ ]:


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

