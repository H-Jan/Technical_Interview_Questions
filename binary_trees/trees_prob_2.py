'''
Given a binary search tree containing integers and a target integer, 
come up with an efficient way to locate two nodes in the tree whose sum 
is equal to the target value.
'''
class BSTSum():
    def solBST(self, root1, root2, target):
        nodes1 = self.in_order(root1)
        nodes2 = self.in_order(root2)

        dict = dict()
        for i in nodes1:
            dict[target - i] = 1

        for i in nodes2:
            if i in dict:
                return True
            else:
                return False

    def in_order(self, root):
        nodes = []
        catch = []
        while len(catch) > 0 or root:
            while root:
                catch.append(root)
                root = root.left 
            root = catch.pop()
            nodes.append(root.val)
            root = root.right
        return nodes
        
