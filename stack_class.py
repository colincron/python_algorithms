class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def reverse_string(self, string):
        reverse = ""
        for letter in string:
            self.push(letter)
        for letter in self.items:
            reverse += self.pop()
        return reverse


def reverse(string):
    my_stack = Stack()
    for char in string:             # done n times
        my_stack.push(char)         # 1 time
    out = ""
    while not my_stack.is_empty():  # done n times
        out += my_stack.pop()       # 1 time
    return out

if __name__ == "__main__":
    print(reverse("hello"))

    # 1*n 1*n = 2*n Order of growth is O(n) because loops are independent of each other
    # if loop is embedded in another loop, 

# for i in range(0,n):
#     for j in range(0,n):
#         #do something
#         pass
#     # O(n^2)

