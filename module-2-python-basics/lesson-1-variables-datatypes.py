"""
Module 2 — Lesson 1: Variables & Data Types
Student: Tamsi, Luis Miguel
Date: September 26, 2025

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Variables are like containers that hold values. You can think of them as labeled boxes where you can store different types of data. 
Each variable has a name, and you can use that name to access the data stored inside it. 
Data types refer to the kind of data that can be stored in a variable, such as numbers, text, or true/false values. 
Understanding variables and data types is essential for writing programs because they allow you to store and manipulate data.


============================================
KEY VOCABULARY
============================================
- variable: A named storage that can store values
- data type: Different kinds of values that can be stored in variables
- int: An integer, a whole number (e.g., 1, 2, 3)
- float: A floating-point number, a number with a decimal point (e.g., 1.0, 2.5, 3.14)
- string: A sequence of characters (e.g., "hello", "world")
- boolean: A data type that can be either True or False
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

  
age = 25          
height = 5.9      
name = "Alice"    
is_student = True 
  
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")



input_num1 = int(input("Enter a number: "))
input_num2 = int(input("Enter another number: "))

print(f"The sum of {input_num1} and {input_num2} is {input_num1 + input_num2}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

a common mistake i make is forgetting to use the correct data type for a variable. 
For example, if you try to perform arithmetic operations asking user for input i forget to convert the input string to an integer or float, which can lead to errors
Always ensure that the data type of your variable matches the operation you want to perform.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
