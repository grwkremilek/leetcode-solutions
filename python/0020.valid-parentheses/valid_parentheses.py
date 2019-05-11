#https://leetcode.com/problems/valid-parentheses/

def isValid(s):   
    parents = {')' : '(', '}' : '{', ']' : '['}
    stack = []
    for i in s:
        if i in parents.values():
            stack.append(i)
        else:
            if stack and stack[-1] == parents[i]:
                stack.pop()
            else:
                stack.append(i)
    return not stack
            
   
