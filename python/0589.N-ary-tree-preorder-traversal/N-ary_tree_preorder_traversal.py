#https://leetcode.com/problems/n-ary-tree-preorder-traversal/

#recursion
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

def preorder(root):
    if root:
        nodes = [root.val]
        for child in root.children:
            nodes.extend(preorder(child))
        return nodes
    return []


 #iteration
 """
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

def preorder(root):
     if root:
        stack, traversal = [root], []
        while stack:
            cur = stack.pop()
            traversal.append(cur.val)
            stack.extend(reversed(cur.children))
        return traversal
         return []
    
