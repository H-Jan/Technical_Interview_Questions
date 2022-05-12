'''
Given a binary tree containing numbers, 
find the maximum sum path (the path that has the largest sum of node values). 
The path may start and end at any node in the tree.
'''
'''
class TNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    #Taken from previous problem, sets up our programming
'''
class BSTMaxSum():
    def maxPathSum(self, root):
        self.max_sum = None

        def temp_max(node1, node2):
            if node1 is None:
                return node2
            elif node2 is None:
                return node1
            return max(node1, node2)

        def max_path_sum(node):
            left_sum = temp_max(0, max_path_sum(node.left))
            right_sum = temp_max(0, max_path_sum(node.right))
            self.max_sum = temp_max(self.max_sum, left_sum + right_sum + node.val)
            return node.val + temp_max(left_sum, right_sum)

        max_path_sum(root)
        return self.max_sum