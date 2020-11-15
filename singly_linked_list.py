# A simple Python program to introduce a linked list

# Node Class
class Node:

    # function to initialise the node object
    def __init__(self,data):
        self.data = data # assign data
        self.next = None # Initialize next as null

class LinkedList:

    # Funciton to initialize head
    def __init__(self):
        self.head = None
    
    

# code execution starts here
if __name__ == "__main__":
    # start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    """
    Three nodes have been created.
    We have references to these three blocks as head, second, and third
    """
    llist.head.next = second # link first node with second

    """ 
        Now next of first Node refers to second. So they are both linked.
    """
    second.next = third
    
    my_node = llist.head
    while True:
        if my_node:
            print(my_node.data)
            my_node = my_node.next
        else:
            break
        