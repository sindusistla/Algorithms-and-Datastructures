import itertools

comb=[]
trans=[1,2,3,4,5,6,7,8]
for i in range(0,len(trans)):
    comb+=itertools.combinations(trans, 3)

print(comb)