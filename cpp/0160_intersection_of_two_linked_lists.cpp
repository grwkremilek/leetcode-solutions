#https://leetcode.com/problems/intersection-of-two-linked-lists/

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {    
        
        ListNode  *first = headA;
        ListNode  *second = headB;
        
        if (first == NULL || second == NULL) return NULL;
        
        while (first != NULL && second != NULL && first != second)
        {
            first = first->next;
            second = second->next;
 
            if (first == second) return first;

            if (first == NULL) first = headB;
            if (second == NULL) second = headA;
    }
        
    return first;
    }
};
