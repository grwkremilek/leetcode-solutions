#https://leetcode.com/problems/score-of-parentheses/


def scoreOfParentheses(S):
'''divide and conquer'''
    def get_score(start, end):
        score = bal = 0                         		#score of balanced string S[i:j]
        for i in range(start, end):                   	#iterate string
            bal += 1 if S[i] == '(' else -1
            if bal == 0:								#split to balanced substrings
                score = score+1 if i-start == 1 else score+2 * get_score(start+1, i)	#if length of string == 2, score+1; if longer multiply score
                start = i+1
        return score
    return get_score(0, len(S))



def scoreOfParentheses(S):
'''stack'''
    count = [0]
    for i in range(len(S)):
        if S[i] == '(':
            count.append(0)
        else:
            v = count.pop()
            count[-1] += max(2 * v, 1)
    return count[0]
