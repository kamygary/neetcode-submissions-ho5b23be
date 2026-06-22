"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        anc = set([p])
        while p.parent:
            anc.add(p.parent)
            p = p.parent
        
        while q not in anc:
            q = q.parent
        
        return q
