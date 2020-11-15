def comp(lst):
    """ 
        This function prints the first item O(1)
        Then it prints the first 1/2 of the list O(n/2)
        Then it prints a string 10 times O(10)
    """
    print(lst[0])
    midpoint = len(lst)/2
    for val in lst[:midpoint]:
        print(val)
    for x in range(10):
        print('number')

def matcher(lst,match):
    """ 
        Given a list lst, return a boolean indicating if match item is in the list
    """
    for item in lst:
        if item = match:
            return True
    return False

def printer(n=10):
    """
    Prints 'hello word!' n times
    O(1) space complexity
    """
    for _ in range(n):
        print('Hello World!')

def create_list(n):
    """
    O(n) space complexity
    """
    new_list = []
    for _ in range(n):
        new_list.append('new')
    return new_list