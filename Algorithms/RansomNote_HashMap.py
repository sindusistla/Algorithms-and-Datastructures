
from collections import Counter;

def ransom_note(magazine, ransom):
    CntMag=Counter(magazine);
    CntRan=Counter(ransom);
    #print(CntMag, CntRan)
   # CntMag.subtract(CntRan);
    if (CntRan-CntMag == {}):
        return True;
    else:
        return False;

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")
