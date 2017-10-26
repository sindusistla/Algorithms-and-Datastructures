"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: """

class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node



def has_cycle(head):
    VisitedList={}
    returnValue=0
    if (head== None):
        # No Cycle return 0
        returnValue=0;
    else:
        # list is not empty
        Current=head;
        while(Current.next!= None):
            # Traverse through the list
            # store the data in dictionary
            print(Current.next)
            if (Current.next not in VisitedList):
                #Update Visited list
                VisitedList.update({Current.next:Current.data})
            else:
                # Loop present
                returnValue=1;
                break;
    #print(returnValue);