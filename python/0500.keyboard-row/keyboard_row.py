#https://leetcode.com/problems/keyboard-row/

def findWords(words):
    keyboard = {
        0 : 'qwertyuiop',
        1 : 'asdfghjkl',
        2 : 'zxcvbnm'
    }
    out = []
    for word in words:
        for i in range(3):
            if all(w.lower() in keyboard[i] for w in word ):
                out.append(word)
    return out
