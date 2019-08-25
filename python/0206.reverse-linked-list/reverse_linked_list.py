#https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):
    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur
    return      cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


def reverseList(head, prev = None):
    if not head:
        return prev

    curr, head.next = head.next, prev
    return self.reverseList(curr, head)


def reverseList(head, prev = None):
    node_value = []
    while head:
        node_value.append(head.val)
        head = head.next
    if len(node_value)<1:
        return head
    pointer = result = ListNode(node_value[-1])
    for n_val in node_value[:-1][::-1]:
        pointer.next = ListNode(n_val)
        pointer = pointer.next
    return result
