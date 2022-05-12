'''
 Given a binary search tree, 
 convert it into a sorted doubly-linked 
 list by modifying the original tree nodes 
 (do not create new nodes).
 '''

 class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def TreeToLinkedList(root):
    head = TreeNode(0)
    prev = None
    current = None
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if prev is None:
            pre = node
            head.right = prev
        else:
            prev.right = node
            node.left = prev
            prev = node
        node = node.right
    prev.right = head.right
    head.right.left = prev
    return head