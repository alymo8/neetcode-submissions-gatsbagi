# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # parent -> min() <= p <= max
        curnode = root

        while True:
            if p.val == curnode.val or q.val == curnode.val:
                return curnode
            elif p.val >= curnode.val and q.val >= curnode.val and curnode.right:
                curnode = curnode.right
            elif p.val <= curnode.val and q.val <= curnode.val and curnode.left:
                curnode = curnode.left
            else:
                return curnode
        return curnode

