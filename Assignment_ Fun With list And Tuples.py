#!/usr/bin/env python
# coding: utf-8

# In[14]:


# list
l=[200,500,800,100,50]
print(len(l))
print('max of l',max(l))
print('min of l',min(l))
print('sum of l',sum(l))
print('l in sorted order',sorted(l))
l[3]= 10
print(l)
sorted(l)


# In[43]:


# Tuples
a=(20,60,25,40)
print('after extend', a)
print(len(a))
print('max of l',max(a))
print('min of l',min(a))
print('sum of l',sum(a))
print('a in sorted order',sorted(a))


# In[44]:


# lists 
l1=['pen', 'fan','computer',  'book', 'file']
l1.append('table')
print('after append',l1)
l1.insert(6,'chair')
print('after insert',l1)
b=l1.count('table')
l1.extend(['notebook', 'waterbottle'])
print('after extend',l1)
l1.remove('notebook')
print('after removing',l1)
l1.reverse()
print('after reverse',l1)
print('coount of ',b)
print ('max of l1', max(l1))
print ('min of l1', min(l1))
print('l1 in sorted order',sorted(l1))
l1.clear()
print('after clear',l1)



# In[47]:


# conversion of tuples and list
L1=[10, 30, 30, 50, 20, 40, 11, 22]
T1=tuple(L1)
print (T1)
T1=(10,50,30,40,20)
L1=list(T1)
print (L1)
s1="Hello"
L2=list(s1)
print ('string to list:', L2)
T2=tuple(s1)
print ('string to tuple', T2)


# In[ ]:




