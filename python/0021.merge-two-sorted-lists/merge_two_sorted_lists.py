#https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2



def mergeTwoLists(l1, l2):
    dummyHead = ListNode(-1)
    p1 = l1; p2 = l2
    prev = dummyHead
    while(p1 and p2):
        if p1.val >= p2.val:
            prev.next = p2
            p2 = p2.next
        else:
            prev.next = p1
            p1 = p1.next
        prev = prev.next
        
    if p1 == None:
        prev.next = p2
    else:
        prev.next = p1
    return dummyHead.next
