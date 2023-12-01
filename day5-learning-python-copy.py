l = [1,345.45,'sudh',5+7j , 34]
type(l)
l[0]
l[0:4:2]
l[4]
l[0:3]
l[-1]
l[::-1]
l[::2]
s = 'pwskills'
list(s)
l+list(s)
l[2][0:2]
l1 = [5]
l+l1
l2 = [3,4,5]
l+l2
l*8
l
len(l)
l.append(5)
l.append('pwskills')
l3 =[2,3,4,5]
l.append(l3)
l[4]
l[-1][2]
l.extend('sudh')
l.extend([1,2,3])
s = 'sudh'
l
l + list(s)
l[2][0:3]
l[2][0:2]
l.append(True)
l[5]
str(l[5])[0:2]
l + [5]
l.append(5)
l1 = [9,8,7]
l + l1
l1 * 3
len(l1*3)
l.append(l1)
l.extend('sudh')
l.extend(l1)
# to insert data in a particular index 
l.insert(1,'ananyo')
l.insert(2,[2,3,4])
l.insert(-1,['subho'])
l.insert(0,45)
l.pop()
l.pop()
l.pop(2)
l.pop(3)
l.pop(4)
l
l.remove(45)
l.remove([2,3,4])
l.insert(3,[2,3,4])
l.append(4)
l.remove(4)
l.append(4)
l.append(4)
l.remove(4) # removes only from 1st accurance .
l.reverse()
l[::-1]

l2 = [2 , 8 , 90 , 10 , 9]
l2.sort()
l2
l3 = [34 , 'sudh' , 45 , 12 , 'kumar']
# l3.sort()
l4 = ['data science', 'kumar','pwskills', 'sudh']
l4.sort()
l4.sort(reverse = True)
l4
l4.index('sudh')
l4.count('sudh')
s = 'sudh'
l5 = [3 , 4 ,5 ,6]
l5[0]= 7
l5
s = 'sudh'
# s[0]= 'a' , strings are mutable
s.replace('s' ,'a')
s

# Tuples 

t = (2 , 3 ,4, 5 ,6 , 'sudh' , False , 45+7j , 45.56 , [3,4,5] )
# you can store any type of data under tuples 
type(t)
len(t)
t[0]
t[-1]
t[::-1]
l5[0] = 'sudh'
l5
# t[0] = 'lol'  tuples are immutable 
# tuples are used in password 
t[::-1]
t
t.count(5)
len(t)
t.index(False)

#set
s = {} # blank set = dict 
type(s)
s2 = {2,3,4,55,6}
type(s2)
s3 = {123 , 124 , 'momo' , 'ananyo', 45 + 7j , (2,3,4,5)}
# list is not accepted by set , but tuples are acceptable , list is mutable and set only collects immutable data . 
s4 = {2 , 3 ,4 , 5, 6 , 7 ,3 ,3 ,2 , 4 ,5 }
set(s4)
# set is used to remove all the duplicate data 
s4 = { 2 , 3, 4 ,5 , 'sudh' , "Sudh"}
set(s4)
l6 = [2 , 3, 4, 5 ,6 ,6 , 6, 3 , 2]
l6 = list(set(l6))
l6
# set will not  arrange the data in an assending order  
# it bascially tries to make unordered collection 
s5 = {234 , 45 , 23 , 567 , 45 , 234 ,'abc', 456}
# set never arranges a data .  
# s5[0]  , set object is not subscriptable , indexing and slicing operation is not possible 
s5.add(4)
s5
# if not available it will add a data 
s5.remove(234)
s5
# in case of set you cant use indexing 
# it supports hasing 
# hasing and indexing are different 
s5.remove(4)
s5
s = 'pwskills '
l = [1 , 345 , 45, 'sudh ', True , 6+ 7j , 345.54]
list(s) + l
l[3][0:2]
str(l[4])[0:2]
l1 = [3, 4,5]
l+l1
len(l+l1)
l.append(5)
l.append('sudh')
l.extend('sudh')
l1.extend('lol')
l1.append(9)
l1
l1[3]
l[-1]
str(l[-3])[0:2]
l.extend('9')
l
l.extend('ananyo')
l
l.extend([3,4,5])
l
l.append([False, 2 ,3.4])
l
l.insert(1,43)
l
# insert() helps to insert the data in a given position /index

l.insert(0 , 'ananyo')
l1.insert(-1,'momo')

l1
l1.insert(-2,45)
l1
l1.insert(8,'sex')
l1
l1.remove('sex')
l1
l1.pop()
l1.pop()
l1.pop()
l1.pop(2) ,# it will remove from index 
l
l.pop(-1)
l.pop(-5)
# for  index wise operation use pop()
l.remove('a')
l
l.remove(345)
l
l1.append(['lol',True, 0 , 1.5 ,34 ])
l1
l1[-1].remove(1.5)
l1
l1[::-1] # that never manipulates the data permanently .
l1.reverse() # for permanent reverse .
l1
l1[::-1]
l1
l1.sort()
l2 = [3,4,5,7,6,8]
l2.sort() # sort sorted the things in assending order .
l2
l1*3
l1
len(l)
l.append(5)
l
l.append([3, True , 4.5 , 4+7j])
l
l.extend(['l','i','s','t'])
l
l.append('pwskills')
l
l[-6][2]
l.extend('pwskills')
l
l.pop(-9)
l.remove(345)
l
l.remove(True)
l
l.insert(0,True)
l
l[::-1]
l.reverse()
l
l1.sort()
l1
l2 = [45,34,34.5 , 23 , 27 ,78]
l2.sort()
l2
l3 = [34,'sudh', 45 , 'kumar']
l3
# l3.sort()
l4 = ['pwskills' , 'lab' , 'physics','data science']
l4.sort()
l4
l4.index('pwskills')
l4.count('pwskills')
# how many times the element appears 
s = 'sudh'
s[0]
l5 = [3 , 4,5,7,8]
l5.sort()
l5
l5[0]= 'a'
l5
l5[0] = 30
l5
l6 = ['mutable', 'item' , 'reassignment' , 4 + 7j , 7.09 , 0.00]
type(l6[-1])
s.replace('s' , 'a')
# item reassignment
s

# tuples 
t = ('sudh', True , 45.56 , 45 + 7j )
t 
type(t)
len(t)
t[::-1] # here new object created .
t
s[::-1]
t.index('sudh')
# string and tuple both follows immutablity 
# tuples are immutalbe , lists are mutable 
# we use tuples for password 
# in terms of mutablity and immutablity tuples and strings are same 
t.count('sudh')
t.count(0)
t.index(True)

# set 
s = {}
type(s)
s2 = {2,3,4,5}
type(s2)
# set dont accept set 
# set only takes immutable data type 
s4 = {2,3,4,5,6,7,3,3,3,2,2 }
set(s4)
# removes repetative elements 
s4 = {'sudh' , 56.78 , 'Sudh'}
set(s4)
l6 = [2 ,3 ,4,4,4, 5, 6 ,7 ,8 ,'sudh' ,'sudh']
l6 = set(l6)
list(l6)
list(set(l6))
# some times it looks like set arranges the data in an assending order but its not true 
# set builds always unordered collection 
s5 = {12 , 2, 3, 4,456 , 789 , 'abc'}
s5
# s5[0]  set object is not subcriptable , so indexing or slicing operation is not going to work 
s5.add(43.87)
s5
# s5.add(4)  it will always add an unique element 
# when there is not an order in set{} , you cant do indexing operation 
# hashing and indexing are diff 
s5.remove(4)
