import itertools
import threading


class myThread(threading.Thread):
    def __init__(self, threadID, TransactionList, Pairs):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.Pairs = Pairs
        self.TransactionList = TransactionList

    def run(self):
        # print("Starting ", self.threadID)
        FormPairs(self.threadID, self.TransactionList, self.Pairs)
        # print("Exiting " ,self.threadID)


def Open_file(Transactions):
    filename = "C:\\Users\\sindu\\Google Drive\\Oakland University1\\Operating Systems\\Assignment 2\\TransactionData.txt";

    fileptr = open(filename, "r")
    LineList = []
    count = 0;
    for line in fileptr:
        LineList = list(map(int, line.strip().split(' ')))
        Transactions.append(LineList)
        count = count + 1;
    'Generate threads for list of lists'
    print("Count of lines", count)


def FormPairs(Transactions, Pairs):
    count = 0
    tuplelist = []
    for tranlist in Transactions:
        for i in range(0, len(tranlist)):
            for k in range(i + 1, len(tranlist)):
                for j in range(k + 1, len(tranlist)):
                    tuplelist.append((tranlist[i], tranlist[k], tranlist[j]));

    Pairs.append(tuplelist)


Transactions = []
Pairs = []
Open_file(Transactions)
FormPairs(Transactions, Pairs)
PairsCount = 0
PairDictionary = {}

for PairList in Pairs:
    # We have pairs list her
    # print( "\n",PairList)
    for OnePair in PairList:
        PairsCount = PairsCount + 1;
        if OnePair not in PairDictionary:
            PairDictionary[OnePair] = 1;
        else:
            # That pair is present in the list
            Value = PairDictionary.get(OnePair);
            # Update with new count
            PairDictionary[OnePair] = Value + 1;
# Find max of count
maximum = max(PairDictionary, key=PairDictionary.get)
print("The maximum is :", maximum, PairDictionary[maximum])

print("Pairs Dictionary is formed")
print("Done with the Program")
