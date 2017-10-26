def Open_file():
    filename ="C:\\Users\\sindu\\Google Drive\\Oakland University1\\Operating Systems\\Assignment 2\\TransactionData.txt";
    fileptr=open(filename,"r")
    ListofLines=[]
    LineList=[]
    for line in fileptr:
        LineList= list(map(int, line.strip().split(' ')))
        ListofLines.append(LineList)
    print(ListofLines)
    'Generate threads for list of lists'


def hello():
    print("Hello")
    tuple=(3,);
    tup_3=(2,3)

    tup_3=tup_3+tuple

    print(tup_3)



    print("Max is : ",PairDictionary[max(PairDictionary, key=PairDictionary.get)],max(PairDictionary, key=PairDictionary.get))
    print("No of pairs :",PairsCount)
    #print (PairDictionary)

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1));


key=(1,2)
value=1
dict={}

dict[key]=value

for key,value in dict.items():
    if (2 in key):
        print("Yes")
