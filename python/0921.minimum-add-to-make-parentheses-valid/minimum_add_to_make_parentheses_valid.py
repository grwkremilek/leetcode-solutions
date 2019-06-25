#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

def minAddToMakeValid(S):
        stack = []
        for bracket in  S:
            stack.append(bracket)
            if len(stack) > 1 and stack[-2] == "(" and stack[-1] == ")":
                stack.pop()
                stack.pop()
        return len(stack)
