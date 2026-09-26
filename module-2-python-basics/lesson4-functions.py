"""
Module 2 — Lesson 4: Functions
Student: Tamsi, Luis Miguel
Date: september 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

A function is a reusable block of code that performs a specific task.
Instead of writing the same code or instructions every time we can write a function
once and call it whenever we need it.

A function can get data through parameters and can send a result
back with a return value.

============================================
KEY VOCABULARY
============================================
- function: a reusable block of code that performs a specific task.
- define: to create a function using the def keyword.
- call: to run a function by writing its name followed by parentheses.
- parameter: a named variable in a function definition that receives input.
- argument: the actual value passed to a function when it is called.
- return value: the result a function sends back to the code that called it.
- scope: the part of a program where a variable can be used.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""


def greet_student(name):
    return f"Welcome to Python, {name}!"


student_name = "Luis Miguel"
message = greet_student(student_name)
print(message)

print("Calculate the total cost of an item.")

def calculate_total(price, quantity, discount=0):
    subtotal = price * quantity
    discount_amount = subtotal * discount
    return subtotal - discount_amount


backpack_total = calculate_total(45, 2, 0.10)
print(f"The backpack order total is ${backpack_total:.2f}.")


def is_long_word(word, minimum_length):
    return len(word) >= minimum_length


word = "function"
if is_long_word(word, 8):
    print(f"'{word}' has at least eight letters.")
else:
    print(f"'{word}' has fewer than eight letters.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

At first, I used print inside a function when I needed to use the answer in
another calculation. Printing only displays a value on the screen, but return
sends the value back so the rest of the program can store or use it. I learned
to use return when a function needs to produce a result, and print when I only
need to show something to the user.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
"""
