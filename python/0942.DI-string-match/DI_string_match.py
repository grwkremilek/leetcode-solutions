#https://leetcode.com/problems/di-string-match/

def diStringMatch(S:):
    left = right = 0
    out = [0]
    for i in S:
        if i == "I":
            right += 1
            out.append(right)
        else:
            left -= 1
            out.append(left)
    return [i - left for i in out]
        
def diStringMatch(S):
    i=0; j=len(S)
    out=[]
    for x in S:
        if x=='I':
            out.append(i)
            i+=1
        else:
            out.append(j)
            j-=1
    out.append(j)
    return out
