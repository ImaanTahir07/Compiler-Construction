

from ReadInput import readInput
from WordBreakers import word_breakers
from LanguageSpecsForToken import language_specs_for_token

input_file_path = "/Users/emaantahirkhan/Desktop/Compiler-Construction/input.x"
output_file_path = "/Users/emaantahirkhan/Desktop/Compiler-Construction/output.x"

sourceCode = readInput(input_file_path)

if sourceCode is not None:
    breakedWords = word_breakers(sourceCode)
    classifiedToken = language_specs_for_token(breakedWords)

    # Writing the lexical output to the output file
    try:
        with open(output_file_path, 'w') as outputfile:
            outputfile.write(str(classifiedToken))  # Convert to string if it's a list or other data type
        print(f"Lexical analysis output written to {output_file_path}")
    except IOError:
        print(f"Error: Unable to write to the file '{output_file_path}'.")
else:
    print("Error: Source code could not be read.")
