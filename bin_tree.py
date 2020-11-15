class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.parent = None
    

def traverse_tree(node):
    if not node:
        return
    print(node.val)
    print("------")
    print("/\t \\")
    print("%s\t %s" % (node.left.val, node.right.val))
    if self.left:
        return traverse_tree(node.left)
    if self.right:
        return traverse_tree(node.right)
    else:
        return traverse_tree(node.parent)


if __name__ == "__main__":
    root = Node(1)     # create root 
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    traverse_tree(root)

    # breadth first search algorithm to make a tree diagram