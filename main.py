"""Simple Boolean Expression Recursive descent interpreter

This interpreter can be called from the command line with
only one argument specifying the file location.
Interpreter can also be called without file location,
in such case, the interpreter will prompt the user
for a file location or a string to be checked

Author: N'Godjigui Junior Diarrassouba
"""

from lexicalanalysis import LexicalAnalyser
from syntaxanalysis import SyntaxAnalyser
from errors import SyntaxError
from pathlib import Path

commands = ["eval ","open ","exit"]

message = """Boolean Expression recursive descent interpreter |  
Type \'eval <boolean expression>\' to evaluate the boolean expression |  
or Type \'open <filename>\' to input a file
directly in this shell. Type \'exit\' to quit the interpreter"""

shell_indicator = "boolex> "

def print_error(input):
    print('\'{}\' is not recognized as an internal command. Valid commands are:'.format(input))
    print(commands)

def run_interpreter(inpt):
    LA = LexicalAnalyser(inpt)
    SA = SyntaxAnalyser(LA)

    try:
        print(SA.run())
    except SyntaxError as ed:
        print(str(ed))

if __name__ == "__main__":
    print(message)
    inpt = input(shell_indicator)
    while inpt:
        input_content = ""
        if inpt.lower().strip() == commands[2]:
            break
        elif inpt.lower().strip()[:len(commands[0])] == commands[0]:
            input_content = inpt.strip()[len(commands[0]):]
        elif inpt.lower().strip()[:len(commands[1])] == commands[1]:
            path_name = Path(str(inpt.lower()[len(commands[1]):]))
            try:
                with open(path_name, 'r') as file_in:
                    input_content = file_in.read()
            except:
                print("No such file found: " + str(path_name))
        else:
            print_error(inpt)

        if input_content != "":
            run_interpreter(input_content)

        inpt = input(shell_indicator)

