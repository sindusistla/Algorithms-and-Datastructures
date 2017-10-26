def IsVisited(VisitedLIst,item):
    if (item in VisitedLIst):
        present=True
    else:
        present=False
    return present;

def ransom_note(magazine, ransom):
    valid=True
    Visited=[]
    for x in ransom:
        # Compare each and every word in ransom to magazine
        if(IsVisited(Visited,x) == False):
            #print(x, magazine.count(x), ransom.count(x))
            if (len(x)<= 5  and len(x)>=1):

                maz_count=magazine.count(x);
                if (maz_count>0):
                    #string is present
                    if(maz_count < ransom.count(x)):
                        valid=False
                        break;
                else:
                    #print(x)
                    valid = False
                    break;
            else:
                print(x)
                valid = False
                break;
            Visited.append(x);
    #print(len(Visited))
    return valid

m, n = map(int, input().strip().split(' '))

if (((m <=30000)and (m>=1)) and ((n <=30000)and (n>=1))):
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if (answer):
        print("Yes")
    else:
        print("No")

