#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


A = np.random.randint(0,5,(8,3))


# In[4]:


A


# In[5]:


B = np.random.randint(0,5,(2,2))


# In[6]:


B


# In[7]:


C = (A[..., np.newaxis, np.newaxis] == B)


# In[8]:


C


# In[9]:


rows = (C.sum(axis=(1,2,3)) >= B.shape[1]).nonzero()[0]
print(rows)


# In[ ]:




