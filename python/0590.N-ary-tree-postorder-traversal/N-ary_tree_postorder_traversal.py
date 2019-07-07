#https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

def postorder(root):
    if root:
        nodes = []
        for child in root.children:
            nodes.extend(postorder(child))
        nodes.append(root.val)
        return nodes
    return []

def postorder(root):
    return [] if not root else [j for i in root.children for j in postorder(i)] + [root.val]
