""" Node is defined as"""


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def check_BinaryProperty(self):
        if (self.left!= None):
            if(self.left.data > self.data):
                return False;
        if(self.right != None):
            if(self.right.data < self.data):
                return False
        return True;

def checkBST(root):
    # Check this in inorder way of traversal
        if (root.data != None):
            # check the right and left nodes
            if (root.check_BinaryProperty()):
                # traverse through left to cover all nodes
                root=root.left

                if (root.left!=None):
                    print(root.data)
                    checkBST(root);
                root=root.right;
                if(root.right!=None):
                    print(root.data)
                    checkBST(root);
            else:
                return False;
        else:
            return False;

        return True;
