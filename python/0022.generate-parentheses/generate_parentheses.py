#https://leetcode.com/problems/generate-parentheses/


#brute force + library
def generateParenthesis(n):
	results = []
    brackets = ['(', ')'] * n
    for br in set(itertools.permutations(brackets)):
        balance = 0
        for b in br:
            balance = balance + 1 if b == '(' else balance - 1
            if balance < 0:
                break
        if balance == 0:
           results.append(''.join(br))
    return results


#brute force
def generateParenthesis(n):
    
    def generateBrackets(brackets = []):
        if len(brackets) == 2*n:
            if isValid(brackets):
                ans.append("".join(brackets))
        else:
            brackets.append('(')
            generateBrackets(brackets)
            brackets.pop()
            brackets.append(')')
            generateBrackets(brackets)
            brackets.pop()

    def isValid(brackets):
        balance = 0
        for c in brackets:
            balance = balance + 1 if c == '(' else balance - 1
            if balance < 0: return False
        return balance == 0
    
    ans = []
    generateBrackets()
    return ans


#backtracking
def generateParenthesis(n):
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2 * n:
            ans.append(S)
            return
        if left < n:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)
    backtrack()
    return ans


#closure number (dynamic programming)	
def generateParenthesis(n):
    if n == 0: return ['']
    ans = []
    for c in range(n):
        for left in self.generateParenthesis(c):
            for right in self.generateParenthesis(n-1-c):
                ans.append('({}){}'.format(left, right))
    return ans
