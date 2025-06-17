# Daily Task3
# Descriptive Question:
# Decorator Function?  Explain with example
# A decorator in Python is a function that takes another function as an argument, extends its behavior, and returns a new function.
# Decorators are often used to add functionality to existing functions in a clean and readable way.
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("Wrapper executed before {}".format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function
# @decorator_function
# def display():
#     print("Display function executed")
# display()

# Coding Question:
# Write a program to find the maximum length word from the given string?
def find_max_length_word(input_string):
    words = input_string.split()
    max_length_word = max(words, key=len)
    return max_length_word
# Example usage
input_string = "Python is a powerful programming language"
max_length_word = find_max_length_word(input_string)
print("The maximum length word is:", max_length_word)
