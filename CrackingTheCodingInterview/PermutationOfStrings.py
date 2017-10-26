# Permutation of strings

def Check_PermutationOfStrings_SortMethod(strA,strB):
    strA=sorted(strA);
    strB=sorted(strB);
    if(strA==strB):
        print("THey are palindromes");
    else:
        print("Not palindromes")

def CounttheCharsInString(Inputstr,charArr):
    for i in Inputstr:
        LetterCount=0
        for j in range(0,len(Inputstr)):
            if(Inputstr[j]==i):
                LetterCount=LetterCount+1;
        charArr[i]=LetterCount

def Check_CharacterCount(strA,strB):
    charArrA={};
    charArrB={};
    if (len(strA)==len(strB)):
        CounttheCharsInString(strA, charArrA)
        CounttheCharsInString(strB,charArrB)
        if(charArrA==charArrB):
            print ("are palindromes")
        else:
            print("Not palindromes")



print("Enter String A")
strA=input();
print("Enter String B")
strB=input();
#Check_PermutationOfStrings_SortMethod(strA,strB);
Check_CharacterCount(strA,strB);
