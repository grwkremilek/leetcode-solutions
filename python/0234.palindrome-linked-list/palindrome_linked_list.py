#https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def isPalindrome(head):
    vals = []
    while head:
        vals += head.val,
        head = head.next
    return vals == vals[::-1]
