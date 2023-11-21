a = 10
a1 = 'c'
type(a1)
int('123')
# int('abcd') 
# this is entirely in str 

print('hello world ! ')
print(123)
print('my age is 23 ')
age = 32
print('my age is :',age)
print(f'my age is:{age}')
# f string in python 

# format() 
# in python we start indexing from 0 
name = 'momo'
age = 32 
print('my name is {} and my age is {}'.format(name,age))
# format function 
# place holder  
print('my name is {firstname} and my age is {firstage}'.format(firstage = age , firstname = name))

# practice 
name = 'ananyo'
age = '23'
degree = 'B.S'
print("my name is {} \n I'm {} years old \n and I'm graduated from IITM with {}".format(name,age,degree))

# control flow 
#    decision making statement 

# if statements 
age = 18
if age <=18 :
    print('you are not eligble to vote .')

if age < 18 :
    print('you are not eligble to vote .')

input()
name = input('enter the name')
age = int(input('enter your age'))

# Task
age12 = int(input('enter your age'))
if age12 >= 18 and age12 <= 42 :
    print('you are young blood !')

#  python variable .
# naming convention are present  there 
a = 1 
# you dont have to write the data type 
type(a)
b = 'sudh'
type(b)
c = 45.678
type(c)
# assignment operator =
sudh = 3535 
type(sudh)
d = True
e = False 
type(d)
type(e)
True - False 
True * False
# True /False 
f = 5 + 4j
type(f)
# f = complex number 
# g = 6 + 7i , it will not recognise , imaginary part denoted by j only 
# you cant use numeric data for variable naming 
# variable naming cant start with special  characters 

_a = 67 
# it will work here 
f.imag
f.real

# mutable and immutable objects 

s1 = 'sudhangsu'
type(s1)
l = [2, 3, 4.5 , "loot" , 3 +7j , 34.45j ]
l[0]
l[-4]
l[1] = 300
l
l[5] = 'pwskills'
l
# you can change the data on particular index 

s1 
# s1[1] = m , string is immutable object basically  you cant mutate at a particular index .

# operators 
# arithmatic operators 
1 + 2  # addition operator
1 - 2  # 
1 * 8 # multiplication opt 
1/2 # divitional opt
1%4 # modulus opt
5%4
5//4 # floor
2**8 # exponantial operator 

## comparison operator 
1>2
1 < 2 
1 == 2
1 == 1
1!=2
# ! = not 
2 > 1 
2 >= 1
2 >= 2 
2 <= 2

# logical operators 
True and True 
True and False 
False and False 
False and True 
1 and 0 
0 and 0 
0 and 1 
1 or 0
0 or 1 
1 or 1 
0 or 0 
True or False 
True or True
# True = 1 and False = 0 

# Bit wise operator 
10 & 4 
bin(10)
bin(4)

13 & 12
bin(13)
bin(12)

11 | 6
bin(11)
bin(6)
bin(15)
# ~ bit wise not 

~12
bin(12)
# -(1100 + 1)
# ~ negation operator 
a = 8
#  right shift operator 

a >> 2
bin(2)
bin(8)

# left shift operator 

20 << 2
bin(20)
bin(80)

k = 10
k += 1
k
k -= 1
k

# conditions 

# if statement 

