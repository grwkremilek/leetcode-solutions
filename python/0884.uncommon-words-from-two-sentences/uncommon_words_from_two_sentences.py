#https://leetcode.com/problems/uncommon-words-from-two-sentences/

def uncommonFromSentences(A, B):
    lst = A.split() + B.split()
    d = {}
    for word in lst:
        d[word] = d.get(word, 0) + 1
    return [k for k,v in d.items() if v == 1]

def uncommonFromSentences(A, B):
    c = collections.Counter((A + " " + B).split())
    return [w for w in c if c[w] == 1]
