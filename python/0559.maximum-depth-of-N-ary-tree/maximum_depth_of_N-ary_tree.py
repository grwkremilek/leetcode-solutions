#https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

def maxDepth(root):
    if not root: return 0
    if not root.children: return 1
    return max(self.maxDepth(node) for node in root.children) + 1
