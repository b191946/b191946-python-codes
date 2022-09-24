#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# BASICS

# In[2]:


a=np.array([1,2,3],dtype="int16")
print(a)


# In[3]:


b=np.array([[9.1,4,6.0,7],[3,4,2,1],[1,9,4,5]])
print(b)
c=np.array([[[1,2,3],[3,5,6],[4,7,8]]])
print(c)


# In[4]:


# Get dimension
a.ndim


# In[5]:


b.ndim


# In[6]:


c.ndim


# In[7]:


#get shape
a.shape


# In[8]:


b.shape


# In[9]:


c.shape


# In[10]:


#get type
a.dtype


# In[11]:


#get size
a.itemsize


# In[12]:


b.itemsize


# 8 bytes

# In[13]:


#get m*n
a.size


# In[14]:


b.size


# In[15]:


c.size


# total size=m*n

# In[16]:


#get total size
a.nbytes


# In[17]:


b.nbytes


# nbytes=size*itemsize

# Accessing /changing specific elements, rows, columns, etc

# In[18]:


a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)


# In[19]:


a[1,5]


# In[20]:


a[0,5]


# In[21]:


#get a specific row


# In[22]:


a[0,:]


# In[23]:


#get a pecific column
a[:,2]


# getting a little more fancy [startindex:endindex:stepsize]

# In[24]:


a[0,1:6:2]


# In[25]:


a[0,1:-1:2]


# In[26]:


a[1,5]=20
print(a)


# In[27]:


a[:,2]=[1,2]
print(a)


# In[28]:


b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# In[29]:


#get specific element(work outside in)
b[0,1,1]


# In[30]:


b[1,0,1]


# In[31]:


b[:,1,:]


# In[32]:


b[:,0,:]

#replace
# In[33]:


b[:,1,:]=[[9,9],[8,8]]
print(b)


# INITIALIZING DIFFERENT TYPES OF ARRAYS
#all 0s matrix
np.zeros((10,10))
# zeros matrix

# In[34]:


# 1s matrix
np.ones((4,5,2))


# In[35]:


#any other number
np.full((2,4),3)


# In[36]:


#any other number (full_like)
np.full_like(a,5)


# In[37]:


# random decimal numbers
np.random.rand(4,2,3)


# In[38]:


np.random.random_sample(a.shape)


# In[39]:


# random integer values
np.random.randint(10,size=(4,3))


# # identity matrix
# 

# In[40]:


np.identity(3)


# # repeat  an array

# In[41]:


arr=np.array([1,2,3])
r1=np.repeat(arr,4)
print(r1)


# # repeat for 2d we use axis=0

# In[42]:


#2d
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)


# In[43]:


output=np.ones((5,5))
print(output)
z=np.zeros((3,3))
z[1,1]=9
print(z)
output[1:-1,1:-1]=z
#output[1:4,1:4]=z is same
print(output)


# # be care when copying arrays!!!

# In[44]:


a=np.array([1,2,3])
b=a.copy()
b[0]=100
print(b)
print(a)


# # Mathematics
# 

# In[45]:


a=np.array([1,2,3,4])
print(a)


# In[46]:


a+2


# In[47]:


a-2


# In[48]:


a*2


# In[49]:


a/2


# In[50]:


b=np.array([1,2,3,4])
a+b


# In[51]:


a**2


# In[52]:


#take the sin
np.sin(a)


# # linear algebra

# ### matrix multiplication

# In[53]:


a=np.ones((2,3))
print(a)
b=np.full((3,2),2)
print(b)
np.dot(a,b)


# ## determinant

# In[54]:


c=np.identity(3)
print(c)
np.linalg.det(c)


# ## statistics

# In[55]:


stats=np.array([[2,2,3],[4,5,6]])
print(stats)


# In[56]:


np.min(stats)


# In[57]:


np.min(stats, axis=1)


# In[58]:


np.min(stats,axis=0)


# In[59]:


np.max(stats)


# In[60]:


np.max(stats,axis=0)


# In[61]:


np.sum(stats,axis=0)


# In[62]:


np.sum(stats,axis=1)

# reorganizing
# In[74]:


before=np.array([[1,2,3,4],[5,6,7,8]])
print(before.shape)
after=before.reshape((2,2,2))
print(after)


# ### vertical and horizontal stacking vectors

# In[75]:


v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(v1)
print(v2)


# In[78]:


np.vstack([v1,v2,v1,v2,v1])


# In[81]:


np.hstack((v1,v2))


# In[82]:


h1=np.ones([2,4])
h2=np.zeros([2,2])
np.hstack([h1,h2])


# # miscellaneous
# ### load data from file
# #### f=np.genfromtxt('name of the file',delimeter=',')
# #### f.astype('int32')

# f[f>50]

# In[ ]:




