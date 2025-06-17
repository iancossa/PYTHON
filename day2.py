'''
a ={1,23,43,65,12}#-> unordered, immutable() and unique
a.add(15)
print(a)
a.remove(43)
print(a)
b = set()
#b ={14}
b.add(123)
print(b)
a.discard(5)#item not in set -> no error -> discard
print(1 in a)
print(len(a))
print(len(b))
print("--SET METHODS--")
a.add(6)
a.update()
print(a)
a.remove(12)
a.discard(89)
a.update(b)
print(a)
a.pop()
print(a)
a.copy()
print(a)

print("--SET MATH OPS--")
e = {1,2,3,4}
f = {3,4,5,6}
print(e|f)#union
print(e.union(f))#union
print(e&f)#intercection
print(e-f)#difference-> values present only on the left set
print(f.difference(e))
print(e^f)#symmetric difference
#frozen set are items that cannot be modified enven with methods
g =frozenset([1,23])
'''
'''
print("---DICTIONARY---")#unordered,mutable,unique,key-value pairs(each key are unique)
#used to store values like map

f={"name":"Ian","age":"24","course":"Python"}
print(f["name"])
f["course"]="Node Js"
print(f)
#Accessing values 
print(f["name"])
print(f.get("age"))
#Adding or updating values
f["name"] = "Luis"
#removing values
f.pop("course")
del f["age"]
print(f)
f.clear()
print(f)


for i in range(1,11):
    print(i)


f={"name":"Ian","age":"24","course":"Python"}

#for printing keys
for k in f.keys():
    print(k)
#for printing the values
for v in f:
    print(f[v])
#for printing the keys and values
for k,v in f.items():
    print(k," : ",v)

#Nested dicionary
snd ={"student":{"name":"Ian","grade":"A"},"student2":{"name":"Tobias","grade":"C"}}
print(snd)
print(snd["student"]["name"])
print(snd["student2"]["grade"])
'''
#STRING - 
'''
a = "Yuri"
b = 'Cherif '
print(b+a)
print(b[-1])
c="""This is a 
multiple 
line
string """
print(c)
e = "abcdefghijklmn"
print(e[8:12])
print(e[9:])

#String methods

stri = "H e l l o"
print(stri.lower())
print("hi".upper())
print("Its me again".title())
print("Let ".strip())
print("car".replace("c","b"))
print(stri.split(" "))
e ="s-p-l-i-t"
print(e.split("-"))
print("hello".join("Guys!"))
joinedstri=stri.split(" ")
print("".join(joinedstri))
print("-".join(joinedstri))
#concatenation
greeting = "Hello"+" "+"World"
print(greeting)
#Repetition
print("ha"*3)
#Membership
print("Py"in "Python")


#Email Validator(Basic Real-Life example)
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print(a+b)

c=int(input("Enter number 1: "))
d=int(input("Enter number 2: "))
print(c*d)

e=float(input("Enter number 1: "))
f=float(input("Enter number 2: "))
print(e*f)

e=float(input("Enter number 1: "))
f=float(input("Enter number 2: "))
print(e/f)
e=float(input("Enter number 1: "))
f=float(input("Enter number 2: "))
print(e**f)

e=float(input("Enter number 1: "))
f=float(input("Enter number 2: "))
print(e%f)
'''
'''email = input("Enter your email:")
if "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")
        
#Logical Operators: we right it and or not

user_age = int(input("Enter your age:"))
if(user_age==18):
    print("This is your first vote")
elif(user_age>18):
    print("You are eligle to vote")
else:
    print("Not eligible to vote!")      
'''
'''
#LOOPS
a=1 
while(a<=5):
    print(a)
    a=a+1      

count =1
while count<=5 :
    print(count)
    count +=1

for l in "Hello":
    print(l)    

for num in range(10):
    if num % 2 == 0:
        continue #skips the iteration
    print(num)

for i in range(10):
    if i==5:
        break
    print(i)

for i in range(1,6):
        if i==3:
            continue
        print(i)

#pass statement
'''
'''
Real Example of ATM
Check if a number is positive,negative or zero
Create a loop that skips multiples of 3
create a loop to stop the loop if the user inputs a negative number

a=int(input("Select a number: "))
if a==0:
    print("The number is iqual to 0.")
elif a>0:
    print("The number is positive")
else:
    print("Negative number")

#Second exercise
for i in range(1,20):
    if i %3==0:
        continue
    print(i)

#Third exercise
a=1
while(a>=0):
    a=int(input("Insert a number: "))
    if(a<0):
        break
    print(a)
    a=a+1
'''
#ATM

def menu():
    balance = 1000
    choice =''
    while choice != '3':
        print("--MENU--")
        print("1. Check Balance")
        print("2. Withdrawal")
        print("3. Exit")
        break
    choice =int(input("Please select a option:"))
    if choice == 1:
        print(balance)
    elif choice == 2:
        a =int(input("Select the amount: "))
        if a > balance:
            print("Invalid amount!")
        else:
            b = balance- a
            print("You withdrew: "+str(a)+"the remaining amount is: "+str(b))
    elif choice == 3:
        print("end")

menu()








