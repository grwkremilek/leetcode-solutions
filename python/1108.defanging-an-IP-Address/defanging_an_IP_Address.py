#https://leetcode.com/problems/defanging-an-ip-address/submissions/

def defangIPaddr(address):
        out = ""
        for i in address:
            if i == '.':
                out += '[.]'
            else:
                out += i
        return out
