# Program to perform string edit

print("Enter Two Strings")
str_A=input()
str_B=input()
OnlyOneEdit=False
if (abs(len(str_A)-len(str_B))==0):
    #The string value is replaces
    #valid to have only one modification
    for i in range(0,len(str_A)):
        #print(str_A[i], str_B[i])
        if(str_A[i]!=str_B[i]):
            #print(str_A[i],str_B[i])
            # found the difference
            if(i==len(str_A)):
                # the last character is different hence
                OnlyOneEdit=True

            if(str_A[i+1:]==str_B[i+1:]):
                # Only one modification
                #print(str_A[i+1:],str_B[i+1:])
                OnlyOneEdit=True
if (abs(len(str_A)-len(str_B))==1):
    # One extra character is present
    # find out which is bigger
    if(len(str_A) > len(str_B)):
        Lesser=len(str_B)
    else:
        Lesser=len(str_A)
    for i in range(0,Lesser):
        #print(str_A[i], str_B[i])
        #print(Lesser)
        if(i==Lesser-1):
            # Last character
            #print("Here lesser")
            if(str_A[i]==str_B[i]):
                # Only last character is different
                #print("Here")
                OnlyOneEdit = True
        if(str_A[i]!=str_B[i]):
            # Compare the strings
            if (str_A[i + 1:] == str_B[i + 1:]):
                # Only one modification
                #print(str_A[i + 1:], str_B[i + 1:])
                OnlyOneEdit = True



print(OnlyOneEdit)
