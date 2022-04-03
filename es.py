#Week 7 task
# Reads in a text file and outputs the number of e'
# Author: Andras Csullog

# It should read in a text file and outputs the number of e'
# The program should take the filename from an argument on the command line.

# Importing this sys library for using it to read the argument from the command line after running the python file
import sys

# Defning the first argument as a file using the argv builtin method
file = sys.argv[1]

# Reading in the file with the builtin open method line by line:
with open(file) as f:
    lines = f.read()

# Defning small and cpital e letters
letter1 = 'e'
letter2 = 'E'

# Count and add e,E letters from each lines:
letterCount = lines.count(letter1) + lines.count(letter2)
# Print the sum  of e and E letters
print(letterCount)


# Used or checked references:
# https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://www.delftstack.com/howto/python/occurrences-of-a-character-in-a-string-in-python/#:~:text=String%20in%20Python.-,Use%20the%20count()%20Function%20to%20Count%20the%20Number%20of,appears%20in%20the%20given%20string.&text=Remember%2C%20upper%20and%20lower%20cases%20are%20treated%20as%20different%20characters.
# https://stackoverflow.com/questions/30768056/importing-external-txt-file-in-python
# https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python

 
