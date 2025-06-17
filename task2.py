# Daily Task2
# Descriptive Question:
# OOPS Principles
# Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design software.
# The four main principles of OOP are:
"""
1.Encapsulation
2.Abstraction
3.Inheritance
4.Polymorphism
"""

# Coding Question:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Sample input
# S=”anagram” t=”nagaram”
# Sample Output:True
# Sample input
# S=”rat” t=”car”
# Sample Output:False

def anagram(s, t):
    l=list(s)
    m=list(t)
    if len(l)!=len(m):
        return False
    for i in l:
        if i in m:
            m.remove(i)
        else:
            return False
    return len(m)==0
print(anagram("anagram", "nagaram"))
print(anagram("rat", "car"))
