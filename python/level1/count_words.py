"""
Create a script that counts the number of words in a given sentence and finds the longest word.
"""

word = input("Enter a sentence: ")

words = word.split(" ")
longest = 0

for x in range(len(words)):
    if len(words[x]) > len(words[longest]):
        longest = x

print("The number of words in the sentence is: ", len(words))
print("The longest word in the sentece is: '", words[longest], "'")
