
'''
#Q1
def gen():
    lst = range(5)
    for i in lst:
        yield i*i
    for i in gen():
        print(i,end="")

#Q2 
i=10
while i>0:
    i-=3
    print("*")
    if i<=3:
        break
else:
    print()

#Q5
a=0
b=a**0
if b<a+1:
    c=1
elif b==1:
    c=2
else:
    c=3
print(a+b+c)

#Q6-recap,q7,q8
#Q9
def search(items,term):
    for i in range(len(items)):
        if items[i]==term:
            print("{0}was found in the list.".format(term))
            break
        else:
            print("{0} was not found in the list.".format(term))

#Q10
start = input("How old were you on your start date?")
end= input("How old are you today ?")
print("congratulations on"+str(int(end)-int(start))+"years of service")
'''