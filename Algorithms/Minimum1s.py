# Find minimum number of 1's in mXn matrix

def CountOnes(start_position,m,a):
    OneCounter=0
    #print("Here")
    #print(start_position,m)
    for i in range(start_position,m+1):
        #print(a[i])
        if(a[i]==1):
            OneCounter=OneCounter+1
            #print(OneCounter)
    return OneCounter

def Calculate():
    n,m=map(int,input().strip().split(' '));
    a = list(map(int, input().strip().split(' ')))
    OneCounterList=[]
    size_array=(n*m)
    maxCountIndex=0
    max=0
    # n rows, m columns
    start_position=0
    End_position=m-1
    if (len(a)== size_array ):
        # Divide the list in sub lists of size m
       max=a[0]
       for i in range(0,n):
           OneCount=CountOnes(start_position,End_position,a)
           if (OneCount < max):
               max=OneCount
               maxCountIndex=i;
           #elif(OneCount == max):
               # The values are equal select the lowest Index

           OneCounterList.append(OneCount);
           start_position=End_position+1
           End_position=End_position+m
       print(OneCounterList,max,maxCountIndex)
        # After counting the Ones
