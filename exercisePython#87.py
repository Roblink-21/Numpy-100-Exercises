#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[24]:


matriz=np.random.randint(0,2, (6,3))
result = np.ascontiguousarray(matriz).view(np.dtype((np.void, matriz.dtype.itemsize * matriz.shape[1])))
_, aux = np.unique(result, return_index=True)
newMatriz =matriz[aux]


# In[25]:


print("=============Matriz Resultante===============")
print(matriz)
print()
print("=============Matriz Resultante===============")
print(newMatriz)


# In[ ]:




