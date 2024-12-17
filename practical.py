#!/usr/bin/env python
# coding: utf-8

# In[1]:


#a -1
user_input = input("Enter elements separated by space: ").split()
print("List:", user_input)


# In[2]:


#a-3

o_list = [1, 2, 3, 4, 5]
t_list = [x * 2 for x in o_list]
print("Original List:", o_list)
print("Transformed List:", t_list)


# In[14]:


#b

def divisible_numbers(n, m):
    result = []
for i in range(1, n + 1):
    if i % m == 0:  # Check if the number is divisible by m
        result.append(i)
return result


# In[6]:


#c 

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

# A. Merge the lists into a dictionary
dictionary = dict(zip(keys, values))
print("Merged Dictionary:", dictionary)

# B. Apply a 10% increase to the values for keys 'a' and 'c'
updated_dictionary = {
    k: (v * 1.1 if k in ['a', 'c'] else v)
    for k, v in dictionary.items()
}
print("Updated Dictionary:", updated_dictionary)


# In[8]:


#a-2

original_list = [2, 6, 3, 8, 5, 10]
squared_list = [x**2 for x in original_list if x > 5]
print("Original List:", original_list)
print("Filtered and Squared List:", squared_list)


# In[ ]:




