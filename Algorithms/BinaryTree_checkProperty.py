""" Node is defined as"""


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def check_BinaryProperty(self):
        if (self.left!= None):
            if(self.left.data >=self.data):
                return False;
        if(self.right != None):
            if(self.right.data <= self.data):
                return False
        return True;

def checkBST(root):
    if (root == None):
        return False;
    if (root.left!= None):
        checkBST(root.left);
    if (root.check_BinaryProperty() != True):
        return False;
    if (root.right):
        checkBST(root.right);

    return True;