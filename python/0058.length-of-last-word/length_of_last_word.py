#https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s):
    if re.search('[a-zA-Z]', s):
        l = s.split()
        return len(l[-1])
    return 0


def lengthOfLastWord(s):  
    s = s.split()
    return len(s[-1]) if s else 0


def lengthOfLastWord(s):  
    if s == '':
        return 0
    elif ' ' not in s:
        return len(s)
    return len(s.strip().split(' ')[-1])
