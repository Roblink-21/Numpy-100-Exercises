#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

Z = np.arange(10000)
np.random.shuffle(Z)
n = 5

# Slow
print (Z[np.argsort(Z)[-n:]])

# Fast
print (Z[np.argpartition(-Z,n)[:n]])


# In[ ]:




