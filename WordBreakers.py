from RegularExpressions import Token, generateToken

def word_breakers(input):
    word = ""
    line = 1
    tokenList = []
    singleBreak = [",",  ";", "(", ")", "{", "}", "[", "]",
                   "-", "+", "*", "/", "%", "=", ">", "<", "@", "!", "."]
    comboBreak = ["||", "&&", ">=", "<=", "!=",
                  "++", "--", "+=", "-=", "*=", "/=", "=="]

    i = 0
    while (i < len(input)):
        checker = input[i]

        # ! checking the next line, carriage return, tab, and space character
        if (checker == "\n" or checker == "\r" or checker == "\t"):
            if (word != ""):
                word, i, current_token = generateToken(word, line, i)
                tokenList.append(current_token)
            else:
                i = i + 1
            line += 1
            continue

        # ! checking for space
        if (checker == " "):
            if (word != ""):
                word, i, current_token = generateToken(word, line, i)
                tokenList.append(current_token)
            else:
                i = i + 1
            continue

        # ! checking for dot and generating token based on the type of value
        if (input[i] == "."):
            if (word != ""):
                # ? If word contains only numbers then dot is a decimal
                if (word.isnumeric()):
                    word = word + input[i]
                    i = i + 1
                # ? If not then word and dot are separate
                else:
                    word, i, current_token = generateToken(word, line, i)
                    tokenList.append(current_token)
                    i = i - 1

            if (i <= len(input)):
                # ? If next character of dot is a number then dot is part of next and word continues
                checking = input[i+1]
                if (input[i+1].isnumeric()):
                    word = word + input[i]
                    i = i + 1
                # ? If next character of dot is not a number then dot is a separate word
                else:
                    word = word + input[i]
                    word, i, current_token = generateToken(word, line, i)
                    tokenList.append(current_token)

            continue
        # ! checking for string with ""
        if (input[i] == "\""):
            if (word != ""):
                word, i, current_token = generateToken(word, line, i)
                tokenList.append(current_token)
                i -= 1

            word = input[i]
            i = i + 1

            # ? String continues till File Ends, Next Double Quote or New Line Character
            while (i < len(input)):
                checking = input[i]
                if (i+1 < len(input)):
                    if (input[i] == "\\"):
                        checking = f"{input[i]}{input[i+1]}"
                        word = word + checking
                        i += 1
                        if (i+1 < len(input)):
                            i += 1
                            continue
                        else:
                            break

                if (input[i] != "\"" and input[i] != "\n"):
                    word = word + input[i]
                    i = i + 1
                else:
                    break

            # if (sourceCode[i] == "\n"):
            #     line += 1

            # ? Breaking String if Double Quote Appear
            if (i < len(input) and input[i] == "\""):
                word = word + input[i]

            word, i, current_token = generateToken(word, line, i)
            tokenList.append(current_token)
            continue

        # ! Combo Breaking Word Appear
        if (i + 1 < len(input)):
            checking = f"{input[i]}{input[i+1]}"
        if (i + 1 < len(input) and f"{input[i]}{input[i+1]}" in comboBreak):
            if (word != ""):
                word, i, current_token = generateToken(word, line, i)
                tokenList.append(current_token)
                i = i - 1

            word = f"{input[i]}{input[i+1]}"
            word, i, current_token = generateToken(word, line, i)
            tokenList.append(current_token)
            i = i + 1
            continue

        # ! Single Character Breaking Word Appear
        if (input[i] in singleBreak):
            if (word != ""):
                word, i, current_token = generateToken(word, line, i)
                tokenList.append(current_token)
                i = i - 1

            word = input[i]
            word, i, current_token = generateToken(word, line, i)
            tokenList.append(current_token)
            continue

        # ? Comment Character Appear
        if (input[i] == "~"):
            if (word != ""):
                word, i, current_token = generateToken(word, line, i)
                tokenList.append(current_token)
            else:
                i = i + 1

            if (i < len(input)):
                checking = input[i]
                # ? Multi Line Comment Characters Appear
                if (input[i] == "~"):
                    i = i + 1
                    # ? Itteration till the Ending Comment character Appear or File Ends
                    while (i < len(input)):
                        checking = input[i]
                        if (input[i] == "\n"):
                            line += 1
                        if (input[i] == "~" and input[i+1] == "~"):
                            i = i + 1
                            break
                        i = i + 1
                    i = i + 1
                    continue

                # ? Single Line Comment Character
                else:
                    # ? Itteration till the line ends or File Ends
                    while (i < len(input)):
                        checking = input[i]
                        if (input[i] == "\n"):
                            line += 1
                            break
                        i = i + 1
                    i = i + 1
                    continue

        # ? Character added to word if no breaking occurs
        word = word + input[i]
        i = i + 1

    # End of File with last word not Breaked
    if (word != ""):
        word, i, current_token = generateToken(word, line, i)
        tokenList.append(current_token)
        
    # End Marker token... to ensure complete tree and complete input parsing

    return tokenList
