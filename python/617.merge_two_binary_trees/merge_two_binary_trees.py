#https://leetcode.com/problems/merge-two-binary-trees/

def mergeTrees(t1, t2):
    if t1 or t2:
        root = TreeNode((t1 and t1.val or 0) + (t2 and t2.val or 0))
        root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return root
