#https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def findMode(root):
    count = {}   
    def DFS(node):
        if node:
            count[node.val] = count.get(node.val,0) + 1
            DFS(node.left)
            DFS(node.right)
    if not root:
        return []
    DFS(root)
    most_frequent = max(count.values())
    res = [n for n,f in count.items() if f == most_frequent]
    return res
