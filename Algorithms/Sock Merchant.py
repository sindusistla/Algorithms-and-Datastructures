
import sys
# Sock Merchant problem solving using hash tabe
class HashMapTable:
    def __init__(self):
        # intialize to a dictionary
        self.Table={};

    def add_key_to_table(self,key):
        if key in self.Table:
            # Increase the count of sock by 1
            self.Table[key]= self.Table[key]+1;
        else:
            self.Table[key]=1;

    def print(self):
        print(self.Table);

    def CountPairs(self):
       pairs=0;
       val=0;
       for i in self.Table:
        val=int(self.Table[i]/2);
        pairs=pairs+val;
       return pairs;

def sockMerchant(n,ar):
    # n: number of given socks
    # ar: input array of given socks
    h = HashMapTable();
    for i in ar:
        h.add_key_to_table(i);
    #h.print();
    print(h.CountPairs());



n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
sockMerchant(n, ar)
