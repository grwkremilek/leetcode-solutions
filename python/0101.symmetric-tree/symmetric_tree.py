#https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def isSymmetric(root):
    if not root: return True
    stack = [(root.left, root.right)]
    while stack:
        cur = stack.pop()
        l, r = cur[0], cur[1]
        if not l and not r: continue
        if not l and r or not r and l or l.val != r.val: return False
        stack.append((l.right, r.left))
        stack.append((l.left, r.right))
    return True
    


def isMirror(node1, node2):
    if not node1 and not node2: return True
    elif (not node1 and node2) or (not node2 and node1): return False
    elif node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left): return True
    else: return False

def isSymmetric(root):
    if not root: return True
    return isMirror(root.left, root.right)
