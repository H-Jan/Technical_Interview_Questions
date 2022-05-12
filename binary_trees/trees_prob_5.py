'''
Given a binary tree, check whether it is a valid binary search tree 
(values in order)
'''

def BST(root):
    def valid_bst(node, right, left):
        if not ((node.val < right) & (node.val > right)):
            return False
        if not node:
            return True
        
        return valid_bst(node.right, right, node.val) & valid_bst(node.left, left, node.val)