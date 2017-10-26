import threading
import time
import operator

exitFlag = 0

class DigitCountThread(threading.Thread):
    def __init__(self, threadID,Digit, PairDictioanry, DigitCount):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.Digit = Digit
        self.PairDictionary = PairDictionary
        self.DigitCount = DigitCount

    def run(self):
        # print("Starting ", self.threadID)
        OccurenceCountDigit(Digit, PairDictionary, DigitCount)

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
            tuplelist.append((TransactionList[i],TransactionList[k]));
    threadLock.acquire()
    Pairs.append(tuplelist);
    threadLock.release();

def OccurenceCountDigit(Digit,PairDictionary,DigitCount):
    Dcount=0;

    for key,value in PairDictionary.items():
        if Digit in key:
            Dcount=Dcount+value;
    threadLock.acquire()
    DigitCount[Digit]=Dcount;
    threadLock.release()

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
DigitThreads=[]
Pairs=[]
PairsList=[]
PairDictionary ={}
DigitCount={}
CheckedDigitList=[]
ProbabilityPairs={}

threadLock = threading.Lock()
#print(Transactions)
# Create new threads for each transaction
#len(Transactions)-1
for trans in range(0,len(Transactions)-1):
    'Create and start threads'
    thread =myThread(trans, Transactions[trans], Pairs)
    thread.start()
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
Digitthread=0
for tranLi in Transactions:
        # find the ocurences
        # create threads
    for Digit in tranLi:
        if Digit not in CheckedDigitList:
            print(Digit)
            Digitthread=Digitthread+1
            threadDigit=DigitCountThread(Digitthread,Digit,PairDictionary,DigitCount)
            threadDigit.start()
            DigitThreads.append(threadDigit)
            CheckedDigitList.append(Digit);
print("Digit thread are created")

for d in DigitThreads:
    d.join();
print("Digit threads are joined")

print(DigitCount)

# Calculate Probability
for key,value in PairDictionary.items:
   if key[1] in DigitCount:
       Occurence=DigitCount[key[1]]
       Probability = Value/Occurence
       ProbabilityPairs[key]=Probability
# Now we have Pair Count in Pair Dictionary and Occurences in DigitCount
# Using these two we need to find probability

print("Exiting Main Thread")
sorted(ProbabilityPairs)