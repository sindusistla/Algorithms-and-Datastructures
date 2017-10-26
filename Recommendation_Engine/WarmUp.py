'''Program to warm up with some exercies using numpy'''

from numpy import *

data=array([[1,2,3],[1,2,3]]);
print (data);

print ("Shape of you ")
print (data.shape)

print ("zeros")
print (zeros((5,4)))

print ("Ones")
print (ones((3,2)))

print ("Random Integers");
rand_matrix=random.randint(10,size=(10,5));
print (rand_matrix);

print ("only column");
print (rand_matrix[0:1,:]);

print ("Only columns 2,3 for row 0")
cols=array([[1,2,3]])
print(rand_matrix[0,cols])

'''Dot product'''

rand_matrix2= random.randint(10,size=(5,2))
print("Random Matrix 2")
print (rand_matrix2)
print ("Dot product is ")
dot_product=rand_matrix.dot(rand_matrix2)
print (dot_product)