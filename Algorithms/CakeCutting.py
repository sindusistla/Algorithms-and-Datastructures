#!/bin/python3

import sys

def howManyToInvite(A, B, a):
    # Return the number of people Leha should invite to his party
    x=A/B;
    return int(a/x)

if __name__ == "__main__":
    A, B, a = input().strip().split(' ')
    A, B, a = [int(A), int(B), int(a)]
    b = howManyToInvite(A, B, a)
    print(b)
