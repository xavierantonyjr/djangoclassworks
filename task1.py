"""
Daily Task1

Descriptive Question:
Major Datatypes in Python?
"""

# Python has several built-in data types that are commonly used. Here are some of the major ones:
# 1.Numeric Types:
#    a)int: e.g: 1, 2, 3
#    b)float: e.g: 1.0, 2.5, 3.14
#    c)complex: e.g: 1 + 2j
# 2.Sequence Types:
#    a)list: e.g: [1, 2, 3]
#    b)tuple: e.g: (1, 2, 3)
#    c)range: e.g: range(5)
# 3. Text Type:
#    a)str: e.g: "Hello, World!"
# 4. Mapping Type:
#    a)dict: e.g: {'key': 'value'}
# 5. Set Types:
#    a)set: e.g: {1, 2, 3}
#    b)frozenset: e.g: frozenset([1, 2, 3])


"""
# Coding Question:

Write a python program that takes a sentence and returns a dictionary where:
a)Keys are words in the sentence.
b)Values are dictionaries with:
    “length”->Length of the word
    “is_palindrome”->True if the word is palindrome,otherwise False.
    “count” ->number of occurrences of the word
"""

def is_palindrome(word):
    return word == word[::-1]

def analyze_sentence(sentence):
    words = sentence.lower().split()
    result = {}

    for word in words:
        if word not in result:
            length = len(word)
            palindrome = is_palindrome(word)
            count = words.count(word)
            result[word] = {
                "length": length,
                "is_palindrome": palindrome,
                "count": count
            }
    return result

sentence = "madam and racecar are level racecar madam"
output = analyze_sentence(sentence)
print(output)

