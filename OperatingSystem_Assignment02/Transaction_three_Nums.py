import threading
import time
import operator

class myThread (threading.Thread):
   def __init__(self, threadID, TransactionList,Pairs):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.Pairs=Pairs
      self.TransactionList=TransactionList

   def run(self):
      #print("Starting ", self.threadID)
      FormPairs(self.threadID, self.TransactionList, self.Pairs)
      #print("Exiting " ,self.threadID)

def FormPairs(threadID, TransactionList, Pairs):
    tuplelist=[]
    for i in range(0,len(TransactionList)):
        for k in range(i+1,len(TransactionList)):
            for j in range(k+1,len(TransactionList)):
                tup = tuple((TransactionList[i], TransactionList[k], TransactionList[j]));
                tuplelist.append(tup)
    threadLock.acquire()
    Pairs.append(tuplelist);
    threadLock.release();
    time.sleep(1)

def Open_file(Transactions):
   filename = "C:\\Users\\sindu\\Google Drive\\Oakland University1\\Operating Systems\\Assignment 2\\TransactionData.txt";

   fileptr = open(filename, "r")
   LineList = []
   count=0;
   for line in fileptr:
       LineList = list(map(int, line.strip().split(' ')))
       Transactions.append(LineList)
       count=count+1;
   'Generate threads for list of lists'
   print("Count of lines",count)

def findCountofA(NumA,Transactions):
    CountA=0
    for tranlist in Transactions:
        for t in tranlist:
            if (t==NumA):
                CountA=CountA+1
    return CountA

def FormTripls(TransactionList):
    tuplelist=[]
    for i in range(0,len(TransactionList)):
        for k in range(i+1,len(TransactionList)):
            for j in range(k+1,len(TransactionList)):
                tuplelist.append(tuple((TransactionList[i], TransactionList[k], TransactionList[j])))

    return tuplelist


# Frist open the file and read the contents into a list of lists
Transactions = []
Open_file(Transactions)
TransactionThreads=[]
DigitThreads=[]
Pairs=[]
PairsList=[]
PairDictionary ={}
CheckedDigitList=[]
ProbabilityPairs={}
countli=0
PairsCount=0
#Transactions=Transactions[0:40]
for tranli in Transactions:
    print(countli)
    countli=countli+1
    Pairs.append(FormTripls(tranli))

for PairList in Pairs:
    for OnePair in PairList:
        PairsCount=PairsCount+1;
        if OnePair not in PairDictionary:
            PairDictionary[OnePair]=1;
        else:
            # That pair is present in the list
            Value=PairDictionary.get(OnePair);
            # Update with new count
            PairDictionary[OnePair]=Value+1;
print("Pairs Dictionary is formed")

'''
threadLock = threading.Lock()
#print(Transactions)
# Create new threads for each transaction
#len(Transactions)-1
Countthread=0
for trans in range(0,len(Transactions)-1):
    'Create and start threads'
    Countthread=Countthread+1
    thread =myThread(trans, Transactions[trans], Pairs)
    thread.start()
    print(Countthread)
    TransactionThreads.append(thread)

for t in TransactionThreads:
    t.join();

print("Completed Joining threads")
PairsCount=0
# Now we have all the pairs in Pairs list add them to a dictionary traverse through the pairs dictionary
# Find the Number of occurences
for PairList in Pairs:
    # We have pairs list her
    #print( "\n",PairList)
    for OnePair in PairList:
        PairsCount=PairsCount+1;
        if OnePair not in PairDictionary:
            PairDictionary[OnePair]=1;
        else:
            # That pair is present in the list
            Value=PairDictionary.get(OnePair);
            # Update with new count
            PairDictionary[OnePair]=Value+1;
print("Pairs Dictionary is formed")

# Find the maximum occurence count of pair
maximum = max(PairDictionary, key=PairDictionary.get)
print("The maximum is :",maximum, PairDictionary[maximum])
# Find the number of occurences of

CountofA=findCountofA(maximum[0],Transactions)
print("-------------- Report-------------------------")
print("Probability of P(%d/%d) -> " %(maximum[1],maximum[0]))
print ("[%d/%d] -> " %(PairDictionary[maximum],CountofA))
print(" -> ",(PairDictionary[maximum]/CountofA))
print("-----------------------------------------------")'''

print("Exiting Main Thread")
