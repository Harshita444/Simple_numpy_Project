#!/usr/bin/env python
# coding: utf-8

# Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
# 
# The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
# 
# The returned dictionary should follow this format:
# {
#   'mean': [axis1, axis2, flattened],
#   'variance': [axis1, axis2, flattened],
#   'standard deviation': [axis1, axis2, flattened],
#   'max': [axis1, axis2, flattened],
#   'min': [axis1, axis2, flattened],
#   'sum': [axis1, axis2, flattened]
# }
# 
# If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

# In[1]:


import numpy as np


# In[2]:


arr=np.arange(9)


# In[4]:


arr


# In[5]:


arr.reshape(3,3)


# In[12]:


import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)
    result = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1), matrix.flatten().mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.flatten().var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.flatten().std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.flatten().max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.flatten().min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.flatten().sum()]
    }
    return result


# In[13]:


calculate([1,2,3,4,5,6,7,8,9])


# In[8]:


jovian.commit()


# In[ ]:




