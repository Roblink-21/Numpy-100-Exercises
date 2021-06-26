#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[11]:


vector=np.random.randint(0,100, (1,9))
matriz= ((vector.reshape(-1,1) & (2**np.arange(8))) != 0).astype(int)


# In[15]:


print("=============Matriz Resultante===============")
print(vector)
print()
print("=============Matriz Resultante===============")
print((matriz[:,::-1]))


# In[ ]:




