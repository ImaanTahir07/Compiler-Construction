import re
from Token import Token

def numberConst(word):
    # This pattern matches both integers and floats
    pattern = r"^[+-]?(\d+(\.\d*)?|\.\d+)$"
    matchPattern = re.match(pattern, word)

    if matchPattern:
        return True
    else:
        return False


def textConst(word):
    # This pattern matches both single characters and strings
    pattern = r"(^'[\\sA-Za-z0-9-!@$#%^&*()+=;:<>,.?/{}[\]|]'$)|(^\".*\"$)"
    matchPattern = re.match(pattern, word)

    if matchPattern:
        return True
    else:
        return False


def isIdentifier(word):
    pattern = "([a-zA-Z_][a-zA-Z0-9_]*)"
    matchPattern = re.match(pattern, word)

    if matchPattern:
        return True
    else:
        return False


def generateToken(word, line, i):
    currentToken = Token(word, line)
    i = i+1
    return "", i, currentToken