# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val < q.val: return self.lowestCommonAncestor1(root, p, q)
        if q.val < p.val: return self.lowestCommonAncestor1(root, q, p)
    def lowestCommonAncestor1 (self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.left == None or root.right == None: return root
        left = root.left.val
        right = root.right.val
        vals = [root.val, left, right]
        print(left, right)
        if p.val in vals and q.val in vals: return root
        elif (root.val == p.val or root.val == q.val) and ((p.val in vals) or (q.val in vals)): return root
        else:
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p,q)
            if p.val < root.val and q.val > root.val:
                return root
            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestro(root.right, p,q)
            
