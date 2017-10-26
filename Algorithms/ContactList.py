class TrieNode:
    def __init__(self):
        # Dictionary of children
        self.children=[None]*26
        self.isleaf=False

class Trie:
    # Data structure class
    def getNode(self):
        return TrieNode();

    def __init__(self):
        self.root=getNode(self);

    def chartoIndex(self,ch):

        return ord(ch)-ord("a");

    def insert(self,key):

        crawler=self.root;
        length=len(key)
        for i in range(0,length):
            # Parse every character of he word
            index=self.chartoIndex(crawler,i);
            # now look for that index in the dictionary of children
            if not crawler.children[index]:
                # then do not add
                crawler.children[index]=self.getNode()
            crawler=crawler.children[index]


n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if (op=="add"):
        # insert the node into the trie
        insertString();
    elif(op=="find"):
        # Find the list of words which start with given substring
        findString();
