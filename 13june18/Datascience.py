
# coding: utf-8

# In[ ]:


import numpy as m
dt=m.dtype([('age',m.int8)])
a=m.array([(10),(20),(30),(40)],dtype=dt)
print(a)
print(a['age'])


# In[ ]:


import numpy as mp   #importing numpy and assigning it to
dt=mp.dtype(mp.int32)
print(dt)


# In[ ]:


import numpy as m
student=m.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)
a=m.array([('abc',19,25.5),('ppp',56,6.5),('jjjj',85,56.6)])
print(a)


# In[4]:


import numpy as mps
x=mps.array([[1,2],[3,4],[5,6]])
y=x[[0,1,2],[0,1,0]]

print(x)
print(y)

