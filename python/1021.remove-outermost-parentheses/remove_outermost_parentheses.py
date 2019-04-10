#https://leetcode.com/problems/remove-outermost-parentheses/

def removeOuterParentheses(S):
    start = 0; close = 0
    primitives = []
    prim = ''
    for bracket in S:
        prim += bracket
        if bracket == '(':
            start += 1;
        elif bracket == ')':
            close += 1;
        if start == close:
            primitives.append(prim)
            prim = ''
            start = 0
            close = 0
    new_primitives = [prim[1:-1] for prim in primitives]
    return ''.join(new_primitives)
