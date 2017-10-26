import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, TransactionsPart,Pairs):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.Pairs=Pairs
      self.TransactionPart=TransactionsPart

   def run(self):
      #print("Starting ", self.threadID)
      FormPairs(self.threadID, self.TransactionPart, self.Pairs)
      #print("Exiting " ,self.threadID)

def FormPairs(threadID, TransactionPart, Pairs):
    tuplelist = []
    print("Thread starting")
    for TransactionList in TransactionPart:
        for i in range(0,len(TransactionList)):
            for k in range(i+1,len(TransactionList)):
                for j in range(k+1,len(TransactionList)):
                    tup= tuple((TransactionList[i],TransactionList[k],TransactionList[j]));
                    tuplelist.append(tup)
    threadLock.acquire()
    Pairs.append(tuplelist);
    print("Thread existing")
    time.sleep(2)
    threadLock.release();

def mythreadExecution( TransactionPart, Pairs):
    tuplelist = []
    count=0
    print("Thread starting")
    for TransactionList in TransactionPart:
        for i in range(0, len(TransactionList)):
            for k in range(i + 1, len(TransactionList)):
                for j in range(k + 1, len(TransactionList)):
                    tup = tuple((TransactionList[i], TransactionList[k], TransactionList[j]));
                    count=count+1;
                    #tuplelist.append(tup)
    #threadLock.acquire()
    #Pairs.append(tuplelist);
    #print("Thread existing")
    #time.sleep(2)'
    print("The count is",count)
    #threadLock.release();

def Open_file(Transactions,linecount):
   filename = "C:\\Users\\sindu\\Google Drive\\Oakland University1\\Operating Systems\\Assignment 2\\TransactionData.txt";

   fileptr = open(filename, "r")
   LineList = []
   for line in fileptr:
       LineList = list(map(int, line.strip().split(' ')))
       Transactions.append(LineList)
       linecount=linecount+1;
   'Generate threads for list of lists'
   print("Count of lines",linecount)


if __name__ == "__main__":

    # Frist open the file and read the contents into a list of lists
    Transactions = []
    linecount=0
    # open file
    Open_file(Transactions,linecount)
    TransactionThreads=[]
    Pairs=[]
    PairsList=[]
    TransactionsPart=[]
    PairDictionary ={}
    threadLock = threading.Lock()
    #print(Transactions)
    # Create new threads for each transaction
    #len(Transactions)-1
    DividePart=linecount;
    startChunk=0
    EndChunk=int(DividePart-1)
    threadcount=0

    #for trans in range(0,7):
        #'Create 8 threads '
        #print("The chunks \n",startChunk, EndChunk)
    TransactionsPart=Transactions[startChunk:EndChunk]
    #thread =myThread(1, TransactionsPart, Pairs)
    #thread.start()
    #TransactionThreads.append(thread)
    mythreadExecution(TransactionsPart, Pairs)
    startChunk=EndChunk;
    EndChunk=startChunk+EndChunk;
    threadcount=threadcount+1
    print("Done with threads")
    #for t in TransactionThreads:
    #thread.join();
        #print("Join")
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