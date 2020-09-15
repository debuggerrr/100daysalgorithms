Problem Statement link:
    https://leetcode.com/problems/binary-tree-pruning/
        
class Solution:
    def pruneTree(self, n):
        if n:
            a,b = n.left,n.right = self.pruneTree(n.left), self.pruneTree(n.right)
            return n if any([a,b,n.val]) else None
