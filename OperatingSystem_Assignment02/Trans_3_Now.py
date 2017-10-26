#
import itertools
from pymongo import MongoClient

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

def FormPairs(Transactions,Pairs,db):
    count=0
    pairs=[];
    for tranlist in Transactions:
        count=count+1;
        Pairs=itertools.combinations(tranlist,3)
        db.triples.insert(Pairs)
        print(count)

# Open File
Transactions=[]
Pairs=[]
Open_file(Transactions)
client = MongoClient("localhost:27017")
myrecord2 = [
        { "author": "Duke II",
          "title" : "PyMongo II 101",
          "tags" : ["MongoDB II", "PyMongo II", "Tutorial II"]
        },
        { "author": "Duke III",
          "title" : "PyMongo III 101",
          "tags" : ["MongoDB III", "PyMongo III", "Tutorial III"]
        }
        ]
db=client.transactionPairs
db.mytable.insert(myrecord2)

print(db.collection_names())
# Now that we have trasaction form pairs of the numbers
FormPairs(Transactions,Pairs,db)