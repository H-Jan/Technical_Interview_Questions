'''
Let’s say a binary tree is "super balanced" 
if the difference between the depths of any two leaf 
nodes is at most one. Write a function to check if a 
binary tree is "super balanced".
'''

def BSTSuper_balanced(root):
    def depth_first_search(root):
        left, right = depth_first_search(root.left), depth_first_search(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]
    return depth_first_search(root)[0]