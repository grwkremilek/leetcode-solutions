#https://leetcode.com/problems/unique-morse-code-words/

def uniqueMorseRepresentations(words):
        MORSE = {    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.', 'f': '..-.', 'g': '--.',  'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---','p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-','v': '...-',  'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..' }
        d = {}
        for word in words:
            trans= []
            for c in word:
                trans.append(MORSE[c])
            translation = ''.join(trans)
            d[translation] = d.get(translation, 0) + 1
        return len(d)


def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    transformations = []
    for word in words:
        trans = ''
        for c in word:
            trans += morse[ord(c) - 97]
        transformations.append(trans)
    return len(set(transformations))


def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    transformations = set()
    for word in words:
        trans = ''
        for c in word:
            trans += morse[ord(c) - 97]
        transformations.add(trans)
    return len(transformations)	
