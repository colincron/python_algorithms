#!/usr/bin/env python3

class Queue2Stacks:
    def __init__(self):
        # Two stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        print("adding %s to stack1 " % element)
        self.stack1.append(element)
        print("stack 1 looks like: %s" % self.stack1)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

def test():
    """ this should print 0,1,2,3,4 
    Note: It will print vertically """
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())

def reverse_a_string():
    my_queue = Queue2Stacks()
    my_string = "hello"
    my_queue.enqueue(my_string)
    my_queue.dequeue()

if __name__ == "__main__":
    test()
    reverse_a_string()
