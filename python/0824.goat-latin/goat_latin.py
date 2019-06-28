#https://leetcode.com/problems/goat-latin/


def toGoatLatin(S):
    def latin(w, i):
        if w[0] not in 'aeiouAEIOU':
            w = w[1:] + w[0]
        return w + 'ma' + 'a' * (i + 1)
    return ' '.join(latin(w, i) for i, w in enumerate(S.split()))
