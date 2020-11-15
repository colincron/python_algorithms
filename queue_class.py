class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# def balance_check(s):
#     if len(s)%2 != 0:
#         return False
#     my_queue = Queue()
#     my_stack = Stack()
#     for i in s:
#         my_queue.enqueue(i)
#         my_stack.push(i)
#     if my_queue.dequeue() == "[" and my_stack.pop() == "]":



def good_balance_check(s):
    if len(s)%2 != 0:
        return False

    opening = set('([{')
    matches = set([('(', ')'), ('[',']'), ('{','}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0


    


if __name__ == "__main__":
    pass
    # print(good_balance_check('[{[{()}]}]'))
    # print(good_balance_check('[{([{])}])'))
