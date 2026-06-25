# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None: return True
        if root == None and subRoot != None: return False
        if root.val == subRoot.val:
            if self.checkSubtree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def checkSubtree(self, p, q):
        if p == None and q == None: return True
        elif p == None and q != None: return False
        elif p != None and q == None: return False
        elif p.val == q.val:
            left = self.checkSubtree(p.left, q.left)
            right = self.checkSubtree(p.right, q.right)
            return (left and right)
