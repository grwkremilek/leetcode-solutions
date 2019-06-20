#https://leetcode.com/problems/repeated-dna-sequences/

def findRepeatedDnaSequences(s):
        d = {}
        for substring in [s[i : i + 10] for i in range(len(s) - 9)]:
            d[substring] = d.get(substring, 0) + 1
        return [k for k, v in d.items() if v > 1]
