

from readSourceCode import readSourceCode
from wordBreaker import breakWords
from classifyToken import classifyToken


print("helllloooo")

input_file_path = "/Users/emaantahirkhan/Desktop/Compiler-Construction/input.x"
output_file_path = "/Users/emaantahirkhan/Desktop/Compiler-Construction/output.x"

sourceCode = readSourceCode(input_file_path)

if sourceCode is not None:
    breakedWords = breakWords(sourceCode)
    classifiedToken = classifyToken(breakedWords)

    # Writing the lexical output to the output file
    try:
        with open(output_file_path, 'w') as outputfile:
            outputfile.write(str(classifiedToken))  # Convert to string if it's a list or other data type
        print(f"Lexical analysis output written to {output_file_path}")
    except IOError:
        print(f"Error: Unable to write to the file '{output_file_path}'.")
else:
    print("Error: Source code could not be read.")
