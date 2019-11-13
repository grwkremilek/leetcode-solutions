#https://leetcode.com/problems/different-ways-to-add-parentheses/

def diffWaysToCompute(input):
    if input.isdigit():
        return [int(input)]
    res = []
    for i in range(len(input)):
        if input[i] in "-+*":
            res1 = self.diffWaysToCompute(input[:i])
            res2 = self.diffWaysToCompute(input[i+1:])
            for j in res1:
                for k in res2:
                    res.append(self.evaluate(j, k, input[i]))
    return res
    
    def evaluate(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
