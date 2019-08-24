#https://leetcode.com/problems/palindrome-linked-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        
        vector<int> numbers;
        while(head)
        {
            numbers.push_back(head->val);
            head = head->next;
        }
        
         for(int i = 0, j = numbers.size() - 1; i < numbers.size(), j >= 0; i++, j--)
         {
             if(numbers[i] != numbers[j]) { return false; }
         }
        
        return true;
        
    }
};
