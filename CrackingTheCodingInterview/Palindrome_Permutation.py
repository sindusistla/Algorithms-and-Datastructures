# Show a string is permutation of Palindrome
# for a string to be palindrome it should have atmost 1 odd number character and rest

def CheckCountofChars(CharCount):
    setOdd=False
    Palindrome=True
    for key in CharCount:
        if(CharCount[key]%2!=0):
            # Count is odd
            if(setOdd==True):
                Palindrome = False;
                break;
            setOdd=True;
    return Palindrome;

print("Enter a string")
str_input=input()
visited=[]
CharCount={}
for i in str_input:
    count=0;
    if (i not in CharCount):
        # Calculate the number of occurences
       CharCount[i]=1;
    else:
        CharCount[i]=CharCount[i]+1;

print(CheckCountofChars(CharCount));