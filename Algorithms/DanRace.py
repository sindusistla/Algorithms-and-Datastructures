#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
drinks=0
# your code goes here
for i in height:
    if ((k-i)<0):
        # needs energy drink
        drinks=drinks+ abs(k-i);
        k=i;
        #print(drinks,k)
print(drinks)