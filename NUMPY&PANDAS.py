import numpy as np
#arr=np.array([1,2,3,4,6])
#arr=np.array([["str","str","str","str","str"],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
#print(arr.ndim)
'''
#Common Creators
arr1=np.zeros((2, 3))
print(arr1)
arr2= np.ones((1,5))
print(arr2)
arr3=np.eye(5)
print(arr3)
arr4=np.arange(3,30,3)
print(arr4)
arr5= np.linspace(10,100,10)
print(arr5)
np.ones((3,))
np.eye(3)
np.arange(1,10,2)#[1 3 5 7 9]start,stop,step
np.linspace(0,1,5)#[0.,0.25,...1]start,stop,number of elements between the limits
'''
'''
#ARRAY MANIPULATION
arr=np.array([[1,2,3],[4,5,6]])
#Indexing & Slicing
print(arr[0,1]) #2
print(arr[:,1]) #[2 5]
#Reshape & Flatten
arr.reshape(3, 2)
arr.flatten()


a=np.array([1,2,3])
b=np.array([[1,2],[3,4]])
print(a.shape)
print(b.ndim)
print(b.dtype)


#ARITHMETIC & BROADCASTING
a= np.array([1],[2],[3])
b =np.array([10,20,30])
print(a*2)
print(np.sqrt(a))
print(a+b)
print(a/b)
'''
#AGREGATE FUNCTIONS
arr= np.array([[1,2],[3,4]])
print(arr.sum())
print(arr.mean())
print(arr.max(axis=0))
print(np.median(arr))

#BOOLEAN INDEXING & FILTERING
a=np.array([1,2,3,4,5])
mask = a >3
print(a[mask])