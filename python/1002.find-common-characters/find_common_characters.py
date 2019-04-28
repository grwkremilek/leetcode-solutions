#https://leetcode.com/problems/find-common-characters/

from functools import reduce
from operator import and_
from collections import Counter

def commonChars(A):
    return list(reduce(collections.Counter.__and__, map(collections.Counter,A)).elements())
