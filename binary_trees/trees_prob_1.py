'''
Given a binary search tree, 
reverse the order of its values by modifying the nodes’ links.
'''

#Binary search tree node with initialized values
class TNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class RevOrder(object):
    def reverseOrder(self, root):
        temp = [root]
        result = []
        while temp:
            next_level = []
            values = []
        #initialization with empty arrays
            for node in temp:
                values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            temp = next_level
            result.append(values)
        return result[::-1]
    #Slice notation to reverse

root = TNode(4)
root.left = TNode(9)
root.right = TNode(20)
root.right.left = TNode(15)
root.right.right = TNode(7)
result = RevOrder().reverseOrder(root)
print(result)
