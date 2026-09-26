"""
Module 2 — Lesson 3: Loops & Lists
Student: Tamsi, Luis Miguel
Date: september 26, 2025

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

Loops are a way to repeat a block of code multiple times. 
They allow you to automate repetitive tasks and iterate through collections of data, such as lists.
There are two main types of loops in Python: for loops and while loops. 

Lists are a type of data structure that can hold multiple values.
You can think of a list as a collection of items, like a shopping list or a to-do list. 


============================================
KEY VOCABULARY
============================================
- list: a variable that can hold multiple values.
- for loop: a control flow statement that allows code to be executed repeatedly for each item in a sequence
- while loop: a control flow statement that allows code to be executed repeatedly as long as a condition is true
- index: the position of an element in a list, starting from 0
- iteration: the process of going through each element in a list or sequence
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

#example of a for loop iterating through a list
onepiece_characters = ["Luffy", "Zoro", "Nami", "Sanji"]
for character in onepiece_characters:
    print(f"I like {character}.")

#example of a while loop iterating through a list using an index
index = 0
while index < len(onepiece_characters):
    print(f"{onepiece_characters[index]} is a character in One Piece.")
    index += 1

    

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

i made a mistake when i was trying to iterate through a list using for loop, my condition was incorrect and it caused an infinite loop.
I learned that it's important to make sure the loop condition is correct and will eventually become false, otherwise the loop will run infinitely.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
