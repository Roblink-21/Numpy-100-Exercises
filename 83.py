#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[9]:


x = np.random.rand(5,7)
get_ipython().run_line_magic('timeit', 'np.power(x,3)')
#1 loops, best of 3: 574 ms per loop
get_ipython().run_line_magic('timeit', 'x*x*x')
#1 loops, best of 3: 429 ms per loop
get_ipython().run_line_magic('timeit', "np.einsum('i,i,i->i',x,x,x)")


# In[ ]:





# In[ ]:




