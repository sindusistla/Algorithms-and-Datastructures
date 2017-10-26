def CheckTheExpression(expression,exp_len):
    retVal=False
    for i in range (0,int(exp_len/2)):
        #print(expression[i],expression[exp_len-i-1])
        if (expression[i] == "{" and expression[exp_len-i-1] =="}" ):
            retVal = True
        elif(expression[i] == "[" and expression[exp_len-i-1] =="]"):
            retVal = True
        elif (expression[i] == "(" and expression[exp_len-i-1] ==")"):
            retVal = True
        else:
            retVal = False
            break;
    return retVal;

def CheckAdjacentBracket(Visited,Bracket):
    exp_len_visited=len(Visited)
    retValue=False
    if(exp_len_visited>0):
        if (Bracket=="}" and Visited[exp_len_visited-1] == "{"):
            #pop the opening bracket from the list
            Visited.remove(Visited[exp_len_visited-1]);
            retValue = True;
        elif (Bracket==")" and Visited[exp_len_visited-1] == "("):
            #pop the opening bracket from the list
            Visited.remove(Visited[exp_len_visited-1]);
            retValue = True;
        elif (Bracket=="]" and Visited[exp_len_visited-1] == "["):
            #pop the opening bracket from the list
            Visited.remove(Visited[exp_len_visited-1]);
            retValue = True;
        ##else:
            # append the closing bracket to the Visited list
            #Visited.append(Bracket);
        return retValue

def is_matched(expression,exp_len):
    Visited=[];
    retValue=True;
    for i in range(0,exp_len):
        if(expression[i]=="{" or expression[i]=="[" or expression[i]=="("):
            # All opening brackets push into visited
            #print(Visited)
            Visited.append(expression[i]);
        elif (expression[i]=="}" or expression[i]=="]" or expression[i]==")"):
            # if closing braces
            #Visited.append(expression[i]);
            #print(Visited)
            retValue=CheckAdjacentBracket(Visited,expression[i]);

    print(Visited)
    if (len(Visited)>0):
        retValue= CheckTheExpression(Visited, len(Visited))

    return retValue


def isMatched(expression,exp_len):
    Stack=[]
    retValue=False;
    for i in range(0, exp_len):
        if (expression[i] == "{" or expression[i] == "[" or expression[i] == "("):
            # All opening brackets push into visited
            # print(Visited)
            Stack.append(expression[i]);
        elif (expression[i] == "}" or expression[i] == "]" or expression[i] == ")"):
            if(len(Stack)==0):
                retValue=False;
                break;
            last_one=Stack.pop();
            #print(last_one,expression[i])
            if (expression[i] == "}" and last_one == "{"):
                # pop the opening bracket from the list
                retValue = True;
            elif (expression[i]==")" and last_one == "("):
                # pop the opening bracket from the list
                retValue = True;
            elif (expression[i]=="]" and last_one == "["):
                # pop the opening bracket from the list
                retValue = True;
            else:
                retValue=False;
                break;
    #print(Stack)
    if(len(Stack)!=0):
        retValue=False;

    return retValue;



t = int(input().strip())
for a0 in range(t):
    expression = list(input().strip());
    exp_len=len(expression)
    if (exp_len%2==0):
        if isMatched(expression,exp_len) == True:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
