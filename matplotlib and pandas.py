#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("shivamani")


# In[3]:



import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv('iris.csv')


# In[4]:


df.head(100)


# In[5]:


variety_count = dict(df["variety"].value_counts())
print(variety_count)


# In[6]:


variety=list(variety_count.keys())
count=list(variety_count.values())
print(variety)
print(count)
varieties=list(df["variety"])
print(varieties)


# In[7]:


fig=plt.figure(figsize=(7,7))
labels=["Iris-setosa","Iris-versicolor","Iris-virginica"]
plt.pie(x=count,labels=labels,
        colors=["blue","orange","green"],
       explode=[0.1,0.1,0.1],
        shadow=True,
       autopct="%0.2f%%")
#plt.xlabel("species")
#plt.ylabel("Iris Species %")
plt.show()


# In[8]:


sl=list(df["sepal.length"])
sw=list(df["sepal.width"])
pl=list(df["petal.length"])
pw=list(df["petal.width"])
print(sl)
print(sw)
print(pl)
print(pw)


# In[9]:


fig=plt.figure(figsize=(10,10))
plt.scatter(sl,sw)
plt.show()


# In[18]:




setosal=list(df["setosa"])


# In[13]:


setosal = []
setosaw=[]
versicolorl = []
versicolorw = []
verginical = []
verginicaw = []
setosapl = []
setosapw=[]
versicolorpl = []
versicolorpw = []
verginicapl = []
verginicapw = []

for i,j,k,l,m in zip(sl,sw,varieties,pl,pw):
    if k == "Setosa":
        setosal.append(i)
        setosaw.append(j)
        setosapl.append(l)
        setosapw.append(m)
    elif k == "Versicolor":
        versicolorl.append(i)
        versicolorw.append(j)
        versicolorpl.append(l)
        versicolorpw.append(m)
    else:
        verginical.append(i)
        verginicaw.append(j)
        verginicapl.append(l)
        verginicapw.append(m)
        
print(setosal)


# In[14]:


fig=plt.figure(figsize=(5,5))
plt.scatter(x=setosal,y=setosaw,color="red")
plt.scatter(x=versicolorl,y=versicolorw,color="green")
plt.scatter(x=verginical,y=verginicaw,color="blue")
plt.legend(["Setosa","Versicolor","Verginica"])
plt.xlabel="sepal length"
plt.ylabel="sepal width"
plt.show()


# In[20]:


plt.bar(x="sw",height=setosal,width=0.2,color="green",columns=[setosal,])
plt.bar(x="versicolor",height=versicolorl,width=0.2,color="orange")
#plt.bar(x="setosa",height=setosal)


# In[ ]:





# In[ ]:





# In[ ]:




