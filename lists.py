# Node Class
class Node:

    # function to initialise the node object
    def __init__(self,data):
        self.data = data # assign data
        self.next = None # Initialize next as null
    
    def deleteNode(self, key):

        # store head node
        temp = self.head

        # if head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
            
        # search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

            # if key was not present in linked list
            if temp == None:
                return
            
            # unlink the node form linked list
            prev.next = temp.next

            temp = None

    def print_list(self):
    # printing list
        node = self # changed node = head to node = self
        while True:
            if node:
                print(node.data)
                node = node.next
            else:
                break

    def remove(self, key):
        node = self

        if node.data == key:
            return node.next

        while True:
            if node:
                node = node.next
            else:
                break
            if node.data == key: # gotta test this --- This is to check second node
                temp = node
                node = node.next
                temp.next = node
                return self.head
                
            # if node.next.data == key:
            #     temp = node
            #     node = node.next.next
            #     temp.next = node
            #     return head
        return head
    
    def get_length(self): # wouldn't need to send head as a parameter
        node = self # node = self.head
        size = 0
        while True:
            if node:
                size += 1
                node = node.next
            else:
                print("Size of Linked List: %s " % size)
                break
        



if __name__ == "__main__":
    head = Node(1)
    node = head
    # list creation
    for index in range(1, 10):
        node.next = Node(index)
        node = node.next
    
    

    node = head                 # points to beginning of list 
    next_node = head.next       # created as reference to the next node
    new_node = Node(10)         # creating a new node with a data value of 10
    node.next = new_node        # head -> next = new_node
    node.next.next = next_node  # head-> next (new_node)-> next = next_node

    #print("The size of my list is: %s " % get_length(head))
    #head.remove(1)
    head.deleteNode(1)
    head.print_list()
    head.get_length()
