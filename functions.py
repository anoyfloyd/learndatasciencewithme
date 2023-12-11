#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('this is very 1st function')


# In[2]:


l = [324 , 45 , 4 + 6j , 23.45 ]


# In[3]:


len(l)


# In[4]:


# functions starts with def key word 


# In[5]:


def test1():
    pass


# In[6]:


def test2():
    print('this is my very 1st function')


# In[7]:


test2()


# In[8]:


# function increases reusablity of your code 


# In[10]:


# test2() + 'momo'
# print gives you 'noneType' data 


# In[11]:


def test2():
    return 'this is my very 1st return .'


# In[12]:


test2() + ' ananyo'


# In[13]:


def test3():
    return 'sudh' , 23 , 345.56 , [12 , 1 ,2, 3]


# In[14]:


a , b , c , d = test3()


# In[15]:


a


# In[16]:


b


# In[17]:


c


# In[18]:


d


# In[19]:


m , n = 9 , 8


# In[20]:


m


# In[21]:


n 


# In[22]:


test3()


# In[24]:


def test4() :
    a = 5 + 6/7
    return a 


# In[25]:


test4()


# In[26]:


def test5(a , b , c):
    d = a -b*c
    return d 


# In[27]:


test5(8,9,10)


# In[29]:


def test6(a , b , d ) :
    c = a + b  + d 
    return c 
    


# In[32]:


test6('Gogol' , ' dutta' , ' maity' )


# In[33]:


test6(1 , 45 , 68.09)


# In[34]:


l = [1,2,3,4 , 'ananyo' , 'momo' ,[1,2,3,4,5,6]]


# In[35]:


l1 = []
for i in l :
    if type(i) == int or type(i) == float :
        l1.append(i)


# # 

# In[36]:


l1


# In[38]:


def test7(l):
    l1=[]
    for i in l :
        if type(i) == list :
            l1.append(i)
        return l1


# In[39]:


l1


# In[40]:


# test7(l)


# In[41]:


l


# In[42]:


def test8(a):
    l1 = []
    if type(i) == list :
        for j in i :
            l1.append(j)
        else :
            if type(i) == int or type(i) == float :
                l1.append(i)
    return l1


# In[43]:


test8(l)


# In[45]:


def test9(a) :
    '''this is my function to extract num data from list'''
    l=[]
    if type(i) == list :
        for j in i :
            l.append(j)
        else :
            if type(i) == int or type(i) == float :
                l.append(i)
    return l


# In[46]:


test9(l)


# In[47]:


l 


# In[49]:


def test10(*args) :
    return args
# to pass n number of data :
# it makes it dynamic 


# In[50]:


test10('ananyo' , 'momo' , 1,2,3 , [1, 2, 3], 45.56)


# In[51]:


def test11(*momo) :
    return momo


# In[54]:


test11(1,2,3)


# In[56]:


def test12(*args , a ) :
    return args , a 


# In[57]:


test12(1,2,3,4 , a = 23)


# In[62]:


def test14(c,d , a = 'ananyo' , b = 'momo') :
           return a , b , c , d


# In[63]:


test14(30 , 'may')


# In[65]:


def test15(**kwargs):
    return kwargs


# In[67]:


test15(a ='momo' , b = 'ananyo' , c = [1,2,3] , d = 30 , e = 'may')


# In[68]:


test15()


# In[69]:


type(test15())


# In[ ]:





# In[ ]:




