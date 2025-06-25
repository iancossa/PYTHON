'''
#Question 6
Val=1
Val2=0
Val= Val^Val2
Val2=Val^Val2
Val=Val^Val2
print(Val)
#0 elevado a 0=0?

#Q7
z,y,x=2,1,0
x,z=z,y
y=y-z
x,y,z=y,z,x
print(x,y,z)#0,1,2

#Q8
a=0
b=a**0
if b<a+1:
    c=1
elif b==1:
    c=2
else:
    c=3
print(a+b+c)

#Q9
i=10
while i>0:
    i-=3
    print("*")
    if i<=3:
        break
else:
    print('*')#3

#Q10
for i in range(1,4,2):
    print("*")
for i in range(1,4,2):
    print("*",end="")
for i in range(1,4,2):
    print("*",end="**")
for i in range(1,4,2):
    print("*",end="**")
print("***)
Q11 pending
#Q12
x="20"
y="30"
print(x>y)
#Q13
s="Hello,Python!"
print(s[-14:15])

#q14
lst=["A","B","C",2,4]
del lst[0:-2]#doubt
print(lst)

#Q15
dict={'a':1,'b':2,'c':3}
for item in dict:
    print(item)#item will print the key

#Q16
s='python'
for i in range(len(s)):
    i=s[i].upper()
print(s,end="")#Terminology: end=, sep= Must recap 

#Q17
lst = [i//i for i in range(0,4)]
sum =0
for n in lst:
    sum += n
print(sum)  # This will raise a ZeroDivisionError for i=0, as division by zero is not allowed

#Q18
lst = [[c for c in range(r)]for r in range(3)]
for x in lst:
    for y in x:
        if y<2:
            print('*', end=" ")#will print * * *

#Q19
lst=[2** x for x in range(0,11)]
print(lst[-1])  # This will print the last element of the list, which is 2**10 = 1024

#Q20
lst1="12,34"
lst2 = lst1.split(",")
print(len(lst1)<len(lst2)) #False 

#Q21
def fun(a,b=0,c=5,d=1):
    return a**b**c

print(fun(b=2,a=2,c=3))
#Q22
x=5
f = lambda x: 1+2
print(f(x))#3

#Q23
from math import pi as xyz
print(pi)# error pi is not defined,should be xyz

#Q24
from random import randint
for i in range(10):
    print(random(1, 5)) #random not defined in the scope, should be randint

#Q25
x=1
def a(x):
    return 2*x
x= 2+ a(x)
print(a(x)) 

#27
a='hello'
def x(a,b):
    z=a[0]
    return z
print(x(a))#error on line 5
'''