#https://leetcode.com/problems/reverse-only-letters/


def reverseOnlyLetters(S):
    S = list(S)
    i, j = 0, len(S)-1
    while i < j:
        while i < j and not S[i].isalpha(): i += 1
        while i < j and not S[j].isalpha(): j -= 1
        S[i], S[j] = S[j], S[i]
        i, j = i + 1, j - 1
    return "".join(S)
