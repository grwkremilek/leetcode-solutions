//https://leetcode.com/problems/symmetric-tree/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
class Solution {
public:
    bool isSymmetric(TreeNode *root) {
        
        if (!root) { return true; }
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* p, TreeNode* q) {
        
        if (!p && !q) { return true; } 
        else if (!p || !q) { return false; }
        
        if (p->val != q->val) { return false; }
        
        return isMirror(p->left,q->right) && isMirror(p->right, q->left); 
    }
};
