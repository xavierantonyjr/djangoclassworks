# Daily Task3
# Descriptive Question:
# Decorator Function?  Explain with example
# A decorator in Python is a function that takes another function as an argument, extends its behavior, and returns a new function.
# Decorators are often used to add functionality to existing functions in a clean and readable way.

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Coding Question:
# Write a program to find the maximum length word from the given string?

text = "This is a simple Python program"
words = text.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)

