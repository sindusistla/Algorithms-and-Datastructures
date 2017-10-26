#!/bin/python3

import sys

def onceInATram(x):
    #retrieve first three and last three digits of the 6 digit number
    str_num=str(x);
    first_three=int(str_num[:0]) + int(str_num[:1])+ int(str_num[:2]);
    last_three=str_num[-3:];

    print(first_three,last_three);
    return result;

if __name__ == "__main__":
    result="";
    x = int(input().strip());
    result = onceInATram(x);
    print(result);
