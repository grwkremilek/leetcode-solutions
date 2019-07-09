#https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverseWords(s):
    words = s.split()
    out = []
    for word in words:
        out.append(word[::-1])
    return ' '.join(out)

def reverseWords(s):
    return ' '.join([word[::-1] for word in s.split()])
