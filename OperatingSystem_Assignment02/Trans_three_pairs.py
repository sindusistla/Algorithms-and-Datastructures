import threading
import time
import pymongo;

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
    tup=()
    for i in range(0,len(TransactionList)):
        for k in range(i+1,len(TransactionList)):
            for j in range(k+1,len(TransactionList)):
                tup = tuple((TransactionList[i], TransactionList[k], TransactionList[j]));
                tuplelist.append((tup));
    threadLock.acquire()
    Pairs.append(tuplelist);
    threadLock.release();

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

# Frist open the file and read the contents into a list of lists
Transactions = []
Open_file(Transactions)
TransactionThreads=[]
Pairs=[]
PairsList=[]
PairDictionary ={}

threadLock = threading.Lock()
#print(Transactions)
# Create new threads for each transaction
#len(Transactions)-1
for trans in range(0,40000):
    'Create and start threads'
    thread =myThread(trans, Transactions[trans], Pairs)
    thread.start()
    TransactionThreads.append(thread)

for t in TransactionThreads:
    t.join();

print("Completed Joining threads")
PairsCount=0
# Now we have all the pairs in Pairs list add them to a dictionary traverse through the pairs dictionary
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

print("Max is : ",PairDictionary[max(PairDictionary, key=PairDictionary.get)],max(PairDictionary, key=PairDictionary.get))
print("No of pairs :",PairsCount)
#print (PairDictionary)


print("Exiting Main Thread")