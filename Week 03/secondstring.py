# python secondstring.py
# Created for Weekly Task 03 06/02/2022
# Write a program that asks a user to input a string and outputs every second letter in reverse order.
# Author: Andras Csullog 
# Please enter a sentence: The quick brown fox jumps over the lazy dog.
# Output: .o zletrv pu o wr cu h


sentence = input("please enter a sentence: ")
stringLength = len(sentence)

reversedSentence = sentence [stringLength::-1]
everySecond = reversedSentence[::2]
print("Your sentence in reversed order and only every second charater:" + everySecond)