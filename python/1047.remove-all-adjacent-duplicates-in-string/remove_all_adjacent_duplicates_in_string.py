#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/		

def removeDuplicates(S):
    stack = []
    for i in range(len(S)):
        stack.append(S[i])
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack = stack[:len(stack)-2]
    return ''.join(stack)


def removeDuplicates(S):
    stack = []
    for c in S:
        stack.pop() if stack and stack[-1] == c else stack.append(c)
    return "".join(stack)
