#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    Max=1;
    count=0;
    # Birthday Candles routine
    for i in range(0,len(ar)):
        if ( ar[i] >=1 and ar[i] <= pow(10,7)):
            if ((ar[i + 1] == Max) or (ar[i]== Max)):
                count = count + 1;
            elif ((ar[i] < ar[i + 1]) and (ar[i+1] > Max)):
                #Update Max
                count=1;
                Max=ar[i+1];
            elif ((ar[i]>ar[i+1]) and (ar[i] > Max)):
                # Update Max
                count = 1;
                Max=ar[i];
    return count;


def birthday(n,ar):
    Max=ar[0];
    count=1;
    for i in range(1,len(ar)):
        if (ar[i] >= 1 and ar[i] <= pow(10, 7)):
            if (ar[i] > Max):
                #Update Max
                count=1;
                Max=ar[i];
            elif (ar[i] == Max):
                count=count+1;
    return count;


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
if (n >=1 and n <= pow(10,5)):
    result = birthday(n, ar)
print(result);
