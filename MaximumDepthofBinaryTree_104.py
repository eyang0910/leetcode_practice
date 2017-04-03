# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """
        if root != None:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            print max(left,right)
        else:
            print 0





root = TreeNode([1,2,3,4])
# print root, root.val
s= Solution().maxDepth(root)

"""
binary tree input and output in three different order

class treenode(object):
    def __init__(self,data=0, left=0, right=0):
        self.data = data
        self.right = right
        self.left = left


class build_tree(object):
    def __init__(self, root=0):
        self.root = root

    # def is_empty(self):
    #     if self.root is 0:
    #         return True
    #     else:
    #         return False

    def tree_gen_pre(self, tn):
        if tn== 0:
            return 'fff'
        else:
            print tn.data
            self.tree_gen_pre(tn.left)
            self.tree_gen_pre(tn.right)

n1 = treenode(1 )
n2 = treenode(2 )
n5 = treenode(5)
n3 = treenode(3,n2,n1)
n4 = treenode('root', n3, n5)

# bt = build_tree(n4)
# bt.tree_gen_pre(bt.root)

build_tree(n4).tree_gen_pre(build_tree(n4).root)

"""