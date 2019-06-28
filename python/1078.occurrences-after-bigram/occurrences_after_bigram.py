#https://leetcode.com/problems/occurrences-after-bigram/

def findOcurrences(text, first, second):
    out = []
    text = text.split()
    for i in range(len(text)-2):
        if text[i] == first and text[i+1] == second:
            out.append(text[i+2])
    return out

def findOcurrences(text, first, second):
    text = text.split()
    return [w3 for w1, w2, w3 in zip(text, text[1:], text[2:]) if w1 == first and w2 == second]
