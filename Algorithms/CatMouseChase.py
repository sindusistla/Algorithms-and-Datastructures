
def FindWinner(x,y,z,winner):
    if (abs(x-z)>abs(y-z)):
        # A is winner
        winner.append("Cat B")
    elif(abs(y-z) > abs(x-z)):
        # B is winner
        winner.append("Cat A")
    elif(abs(y-z) == abs(x-z)):
        # Mouse escapes
        winner.append("Mouse C")
    return winner

winner=[]
q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    FindWinner(x,y,z,winner)
for x in winner:
    print(x)