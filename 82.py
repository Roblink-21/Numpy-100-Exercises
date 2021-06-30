#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[16]:


Z = np.array([("hola", 2.5, 3),
("mundo", 3.6, 2)])
R = np.core.records.fromarrays(Z.T,
names='col1, col2, col3',
formats = 'S8, f8, i8')


# In[17]:


Z


# In[18]:


R


# In[ ]:




