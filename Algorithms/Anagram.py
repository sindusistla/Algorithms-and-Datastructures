def number_needed(a, b):
    # program to find
    elements_matched=[]
    elements_unmatched=[]
    extracount=0
    for x in a:
        # Compare each and every element in a to b
            if (x in b):
                # Elements matched
                if (a.count(x) == b.count(x)):
                    elements_matched.append(x);
                else:
                    # remove extra occurences of the character
                    extracount=abs(a.count(x)- b.count(x)) + extracount
                    print(extracount)
            else:
                elements_unmatched.append(x);
    for x in b:
        if (x in a):
            # Elements matched
            if (a.count(x) == b.count(x)):
                elements_matched.append(x);
            else:
                # remove extra occurences of the character
                extracount = abs(a.count(x) - b.count(x)) + extracount
                print(extracount)
        else:
            elements_unmatched.append(x);
    print (elements_unmatched,elements_matched)
    return (len(elements_unmatched)+extracount)

def Isvisited(visited_arr,element):
    ispresent=False
    if (element in visited_arr):
        ispresent=True
    return ispresent

def print_matched(a,b):
    visited=[]
    elements_matched=[]
    elements_unmatched=[]
    extracount=0
    for x in a:
        if (Isvisited(visited,x)== False):
            if (x in b):
                # Elements matched
                if (a.count(x) == b.count(x)):
                    elements_matched.append(x);
                else:
                    # remove extra occurences of the character
                    extracount = abs(a.count(x) - b.count(x)) + extracount
                    #print(extracount)
                    #print (a.count(x),b.count(x))
            else:
                extracount=extracount+ a.count(x)
                elements_unmatched.append(x);
            visited.append(x);
    for x in b:
        if (Isvisited(visited,x)== False):
            if (x in a):
                # Elements matched
                if (a.count(x) == b.count(x)):
                    elements_matched.append(x);
                else:
                    # remove extra occurences of the character
                    extracount = abs(a.count(x) - b.count(x)) + extracount
                    #print(a.count(x), b.count(x))
                    #print(extracount)
            else:
                elements_unmatched.append(x);
                extracount=extracount+b.count(x)
            visited.append(x)
    #print (visited)
    return ( extracount)


a = input().strip()
b = input().strip()
print(print_matched(a, b))