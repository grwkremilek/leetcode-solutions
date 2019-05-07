#https://leetcode.com/problems/replace-words/

def replaceWords(dict, sentence):
    sentence = sentence.split()
    for d in dict:
        for i in range(len(sentence)):
            if sentence[i].startswith(d):
                sentence[i] = d
    return ' '.join(sentence)
