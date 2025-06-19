'''
#file handling
f=open("note.txt","r")#read
x=f.read()
f=open("note.txt","w")#overwrite
f.write("second note")#overwrite
f=open("note.txt","a")#read,write, append
f.write("\n o que teremos agora ?")
#x=f.read()
#print(x)
f.close()#closing the block manually
'''
#good pratice:

with open("note.txt","r+") as f:
    x=f.read()
    f.seek(0)
    f.write("Fox Comedy")
    #f=open("note.txt","a")
    #f.write("\n The Simpsons")
    print(x)#no need to close the file with block

try:
    with open("missing.txt","r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An I/O error occured.")