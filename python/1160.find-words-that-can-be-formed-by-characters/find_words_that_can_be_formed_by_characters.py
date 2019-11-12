#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

def countCharacters(words, chars):
        res = 0
        for word in words:
            add = True
            for i in word:
                if word.count(i) > chars.count(i):
                    add = False
                    break
            if add:
                res += len(word)
        return res
