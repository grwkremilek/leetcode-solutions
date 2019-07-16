#https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def rangeSumBST(root, L, R):
    out = 0
    def inorderTraversal(root):
        res = []
        if root:
            res = inorderTraversal(root.left) 
            res.append(root.val)
            res = res + inorderTraversal(root.right)
        return res
    for n in inorderTraversal(root):
        if  L <= n <= R:
            out += n
    return out


def rangeSumBST(root, L, R):
    out = 0
    def inorderTraversal(root):
        res = []
        if root:
            res = inorderTraversal(root.left) 
            res.append(root.val)
            res += inorderTraversal(root.right)
        return res
    for n in inorderTraversal(root):
        if  L <= n <= R:
            out += n
    return out


def rangeSumBST(root, L, R):
    if root:
        l = self.rangeSumBST(root.left, L, R)
        r = self.rangeSumBST(root.right, L, R)
        return l + r + (L <= root.val <= R) * root.val
    return 0


def rangeSumBST(root, L, R):
    if not root:
        return 0
    elif root.val >= L and root.val <= R:
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
    elif root.val < L:
        return self.rangeSumBST(root.right, L, R)
    else:
        return self.rangeSumBST(root.left, L, R)


def rangeSumBST(root, L, R):
    if not root:
        return 0            
    def postorder(node, _L, _R):
        ans = 0
        if _R > L and node.left:
            ans += postorder(node.left, _L, node.val)
        if _L < R  and node.right:
            ans += postorder(node.right, node.val, _R)
        if L <= node.val <= R:
            ans += node.val
        return ans        
    return postorder(root, float("-inf"), float("inf"))


def rangeSumBST(root, L, R):
    return root and rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R) + (L <= root.val <= R) * root.val or 0
    
