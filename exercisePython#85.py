#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[7]:


matriz=np.array([(1,1,1),
              (1,1,1),
              (1,2,3)])
newValors= np.logical_and.reduce(matriz[:,1:] == matriz[:,:-1], axis=1)
result=matriz[~newValors]


# In[8]:


print("===========Matriz original==============")
print(matriz)
print()
print("=======filas con valores con valores desiguales===========")
print(result)


# In[ ]:




