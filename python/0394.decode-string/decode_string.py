#https://leetcode.com/problems/decode-string/submissions/

def decodeString(s: str) -> str:
        stack = []; num = ""
        stack.append(["", 1])
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(["", int(num)])
                num = ""
            elif c == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += c
        return stack[0][0]
