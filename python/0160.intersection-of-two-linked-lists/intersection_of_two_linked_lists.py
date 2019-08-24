#https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headA is None or headB is None:
        return None
    
    first = headA
    second = headB
    
    while first != second:
        first = headB if first is None else first.next
        second = headA if second is None else second.next
    return first
