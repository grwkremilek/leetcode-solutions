def uncommonFromSentences(A, B):
    AB = A+" "+B
    bag = list(AB.split())
    return list(filter(lambda x: bag.count(x) == 1, bag))
