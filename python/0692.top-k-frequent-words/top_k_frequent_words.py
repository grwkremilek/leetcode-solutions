#https://leetcode.com/problems/top-k-frequent-words/

def topKFrequent(words, k):
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    d = sorted(d.items(), key=lambda w: (-w[1], w[0]))
    return [x[0] for x in d[:k]]
