'''
print("Hello World")
x = 10
y = 5
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
name ="Ian"
surname = " Cossa"
print(name+surname)

#naming conventions
student ="" #allowed
Studeny ="" #allowed
#Data type in Python:
# int, float, string,boolean,set,dict,list,tuple

name = "Joshua"

print(name)

#functions in python
def greet(): #function definition
    print("Greetings")

greet()

def add(a,b): #a,b parameters
    print(a+b)

add(1,4)#function calling (1,4 -> arguments)

def sub(a,b):
    print(a-b)

def multi(a,b):
    print(a*b)

def div(a,b):
    print(a/b)   

sub(7,8)
multi(9,1)
div(16,2)    

def greeting(nome):
    print("hello " +nome) #nome -> local variable

greeting("Denzel")
print(name) #outside the function

#list
#Array -> collection of homogeneous (same datatypes)
#list -> [1,2,"abc",True,5.22] hetereogeneous datatype

a = [1,2,3,"abc",True,False,1.33]#list in py-> ordered,indexable,can store different datatypes,changeable(you 
#can add, remove,or change elements),Allow duplicated values
#mutable,ordered,duplicates allowed,heterogeneous & Indexable
print(a)
a[3]=4
print(a)
a.append("Lau")#add to the end
a.insert(3,"French")#you choose the index
print(a)

#a.extend()

#removing items
a.remove(4) #removes the value 4
a.pop(2)#by default removes the last element,if I give a value removes the index value
print(a)
a.clear()#clear the entire list
print(a)
numbers=[1,"two",3,"four",5,6,"seven"]
#numbers.sort()
print(numbers)
print(numbers[1:3])#:-> slicing[start:stop-1]

#typecasting 
a = 10
b = "20"
c =False
print(str(a)+b)#concatenation & typecasting(converting int to string)
#print(a+int(b))converting int to str
if(c):#Boolean value of any string is true
    print("c is false")
print(type(c))
print(type(b))#type -> datatype
print(type(a))

arr = [1,2,3,4,5,"1"]
print(arr)
#arr2 = arr shallow copying
arr2 = arr.copy() #deep copy
arr.pop()
print(arr)
print(arr2)

#list methods
fruits = ["banana","apple","cherry",'apple']
fruits.sort()
fruits.reverse
print(fruits.count("apple"))
print(fruits.index("cherry"))

#TUPLES -> duplicates,immutable,ordered(index),reassignable
print("------------")
print(" --TUPLES-- ")
tuples =(1,2,3,3,44,5,6,7)
print(tuples[3])
tuples=(1,2,3,4)# u can reassign the values
print(tuples)
print(tuples[-1])
print(tuples.count(3))#counts the items in the tuple
print(tuples.index(3))#returns the value of the first position

person = ("John",25,"Developer")
name,age,profession = person
print(profession)
print(name)
print(person)
#tuples are faster than lists
'''
#sets -> Unordered, Mutable,No duplicate elements and Elements must be immutable

set1 ={1,2,3,4}
print(set1)
emptyset = set() #create empty set
print(emptyset)
set1.add(10)#via methods-> add/remove values
print(set1)
set1.remove(10)#remove -> removes the items in set
print(set1)