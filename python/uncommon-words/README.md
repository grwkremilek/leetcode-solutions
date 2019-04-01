# Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.) A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words. You may return the list in any order.


example 1:

Input: A = "this apple is sweet", B = "this apple is sour"

Output: ["sweet","sour"]


example 2:

Input: A = "apple apple", B = "banana"

Output: ["banana"]


## comments

Time Complexity: O(M + N), where M, N are the lengths of A and B respectively.

Space Complexity: O(M + N), the space used by count.


#### Runtime: 36 ms (98.39%)
