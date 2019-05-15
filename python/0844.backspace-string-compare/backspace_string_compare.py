#https://leetcode.com/problems/backspace-string-compare/

def backspaceCompare(S, T):
    def fillStack(lst):
        stack = []
        for i in lst:
            if i == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return stack
    return fillStack(S) == fillStack(T)
