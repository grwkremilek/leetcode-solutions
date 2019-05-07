#https://leetcode.com/problems/word-pattern/

def wordPattern(pattern, str):
    words = str.split(' ')
    return len(pattern) == len(words) and len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))
		
		
