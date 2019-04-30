#https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s):
    if re.search('[a-zA-Z]', s):
        l = s.split()
        return len(l[-1])
    return 0
