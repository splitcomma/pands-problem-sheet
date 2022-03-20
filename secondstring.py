# python secondstring.py
# Created for Weekly Task 03 06/02/2022
# Write a program that asks a user to input a string and outputs every second letter in reverse order.
# Author: Andras Csullog 
# Please enter a sentence: The quick brown fox jumps over the lazy dog.
# Output: .o zletrv pu o wr cu h


sentence = input("please enter a sentence: ")
stringLength = len(sentence)

reversedSentence = sentence [stringLength::-2]

print("Your sentence in reversed order and only every second charater:" + reversedSentence)

# Used refenrences:
# https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
# https://stackoverflow.com/questions/46503865/getting-every-nth-character-in-the-string-in-python