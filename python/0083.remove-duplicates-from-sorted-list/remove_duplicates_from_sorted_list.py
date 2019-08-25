https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def deleteDuplicates(head):
    if head == None:
        return head
    cur = head.next
    prev = head
    
    while cur != None:
        if cur.val == prev.val:
            prev.next = cur.next
            cur = cur.next
        else:
            cur = cur.next
            prev = prev.next   
    return head


def deleteDuplicates(head):
    temp=head
    while temp and temp.next:
        if temp.val==temp.next.val:
            temp.next = temp.next.next
        else:
            temp=temp.next
    return head
