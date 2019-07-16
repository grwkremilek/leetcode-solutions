#https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next

def deleteNode(self, node):
    current = node
    after = node.next
    if after != None:
        current.val = after.val
        current.next = after.next
        after = None
