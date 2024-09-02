from RegularExpressions import *

def language_specs_for_token(tokenList):
    # keywords = {"void": "VOID","number": "DT",  "bool": "DT", "text": "DT", "array":"ARRAY",  
    #             "if": "IF", "else": "ELSE", "for": "LOOP", "break": "BREAK", 
    #             "continue": "CONTINUE", "define": "DEFINE", "print": "PRINT",  
    #             "try": "TRY", "catch": "CATCH", "finally":"FINALLY", "class": "CLASS", "error": "ERROR",
    #              "this":"THIS", "true": "BOOL", "false": "BOOL", "return":"RETURN",
    #              "abstract":"ABSTRACT","calling": "CALL_FUNC",  "construct":"CONSTRUCTOR", "method":"METHOD",
    #             "extends" : "EXTENDS"}
    keywords = {
    "empty": "EMPTY",          # void -> empty
    "number": "DATA_TYPE",    # number -> integer
    "boolean": "DATA_TYPE",    # bool -> boolean
    "text": "DATA_TYPE",     # text -> string
    "list": "LIST",            # array -> list
    "condition": "CONDITION",  # if -> condition
    "otherwise": "OTHERWISE",  # else -> otherwise
    "loop": "ITERATION",       # for -> loop
    "exit": "EXIT",            # break -> exit
    "skip": "SKIP",            # continue -> skip
    "declare": "DECLARE",      # define -> declare
    "output": "OUTPUT",        # print -> output
    "attempt": "ATTEMPT",      # try -> attempt
    "handle": "HANDLE",        # catch -> handle
    "conclude": "CONCLUDE",    # finally -> conclude
    "blueprint": "BLUEPRINT",  # class -> blueprint
    "exception": "EXCEPTION",  # error -> exception
    "self": "SELF",            # this -> self
    "yes": "BOOLEAN",          # true -> yes
    "no": "BOOLEAN",           # false -> no
    "give_back": "GIVE_BACK",  # return -> give_back
    "base": "BASE",            # abstract -> base
    "initializer": "INITIALIZER", # construct -> initialize
    "function": "FUNCTION",    # method -> function
    "inherits": "INHERITS"     # extends -> inherits
}


    operators = {"=": "ASSIGN", "+=": "COMBO_ASSIGN", "-=": "COMBO_ASSIGN", "++": "INC_DEC", "--": "INC_DEC", "<": "RELATION", ">": "RELATION",
                 "==": "RELATION", "<=": "RELATION", ">=": "RELATION", "!=": "RELATION", "and": "AND", "or": "OR", "not": "NOT",
                 "+": "PM", "-": "PM", "*": "M_D_M", "/": "M_D_M", "%": "M_D_M", "**": "POWER", "in": "SOMETHING"}

    punctuators = {"(": "O_PARAM", ")": "C_PARAM", "[": "O_BRACK", "]": "C_BRACK", "{": "O_BRACE", "}": "C_BRACE", ":": "COLON",
                   ",": "SEPARATOR", ";": "TERMINATOR", ".": "DOT"}

    for i in range(len(tokenList)):

        if (tokenList[i].value in keywords.keys()):
            tokenList[i].class_part = keywords[tokenList[i].value]
            continue

        if (tokenList[i].value in operators.keys()):
            tokenList[i].class_part = operators[tokenList[i].value]
            continue

        if (tokenList[i].value in punctuators.keys()):
            tokenList[i].class_part = punctuators[tokenList[i].value]
            continue

        if (numberConst(tokenList[i].value)):
            tokenList[i].class_part = "NUM_Constant"
            continue


        if (textConst(tokenList[i].value)):
            tokenList[i].class_part = "TEXT_Constant"
            tokenList[i].value = tokenList[i].value[1:-1]
            continue

        if (isIdentifier(tokenList[i].value)):
            tokenList[i].class_part = "ID"
            continue

        tokenList[i].class_part = "INVALID"

    return tokenList
