'''
This code repo uses some knowledge learned from:
https://www.thefreedictionary.com/Adding-Suffixes-after-Silent-E.htm
https://speakspeak.com/resources/english-grammar-rules/english-spelling-rules/double-consonant-ed-ing
'''

def doubleLastChar(word):
    consonant = "qwrtzpsdfghjklyxcvbnm"
    vowel = "aeiuo"

    word = word.lower()
    thirdLastChar = word[-3:-2]
    secondLastChar = word[-2:-1]
    lastChar = word[-1]

    if (
        thirdLastChar in consonant and
        secondLastChar in vowel and
        lastChar in consonant and
        lastChar != 'w' and
        lastChar != 'y'
    ):
        return True

    return False

def retainE(word):
    if word == 'be':
        return True

    lastTwoChars = word[-2:]
    if lastTwoChars in ['ee', 'oe', 'ye']:
        return True

    return False

def p2pp(word):
    wordLen = len(word)
    if word.endswith("ie"):
        newWord = word[0:wordLen - 2] + "ying"
    elif word.endswith("e") and not retainE(word):
        newWord = word[0:wordLen - 1] + "ing"
    elif doubleLastChar(word):
        newWord = word[0:wordLen] + word[-1] + "ing"
    else:
        newWord = word + "ing"

    return newWord
