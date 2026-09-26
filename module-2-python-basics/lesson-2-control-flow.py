"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Tamsi, Luis Miguel
Date: september 26, 2025

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
Control flow is the order in which a program executes code. It allows you to make decisions in your code based on certain conditions. 
For example, you want to execute a block of code only if a certain condition is met. This is where if, elif, and else statements come in handygit.


============================================
KEY VOCABULARY
============================================
- condition: A statement that evluates to either True or False
- if / elif / else:  
if: executes a block of code if the condition is True. 
elif: executes a block of code if the previous condition was False and the current condition is True. 
else: executes a block of code if all previous conditions were False.
- comparison operator: An operator that compares two values and returns a boolean value.
- boolean expression: An expression that evaluates to either True or False.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
#example of control flow using if, elif, and else statements
age = 25

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#example of control flow using comparison operators


temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("It's hot outside.")
elif temperature > 25:
    print("It's warm outside.")
elif temperature > 25:
    print("It's cool outside.")
else:
    print("It's freezingly cold outside.")


#example of control flow using boolean expressions
is_raining = True

if is_raining:
    print("Don't forget to take an umbrella!")
else:
    print("Enjoy the sunny weather!")
    
    
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
i always forget to use the correct comparison operators in my conditions. 
For example, using a single equal sign (=) instead of a double equal sign (==) for comparison can lead to error. 
Always double-check your conditions to ensure they are written correctly.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
