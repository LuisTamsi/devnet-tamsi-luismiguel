"""
Module 2 — Activity: File Sorting with os and shutil
Student: Tamsi, Luis Miguel 
Date: September 26, 2025

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================

This program organizes files in a specified directory into subfolders based on their file types.
It uses the os module to interact with the file system and the shutil module to move files.


============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

user_input = input("folder Path: ")

if os.path.exists(user_input):
    list_of_items = []
    list_of_items = os.listdir(user_input)

    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0

    if not os.path.exists(os.path.join(user_input, "Images")):
        os.mkdir(os.path.join(user_input, "Images"))

    if not os.path.exists(os.path.join(user_input, "Documents")):
        os.mkdir(os.path.join(user_input, "Documents"))

    if not os.path.exists(os.path.join(user_input, "Videos")):
        os.mkdir(os.path.join(user_input, "Videos"))

    if not os.path.exists(os.path.join(user_input, "Others")):
        os.mkdir(os.path.join(user_input, "Others"))

    for list in list_of_items:

        file_path = os.path.join(user_input, list)

        if list.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            shutil.move(file_path, os.path.join(user_input, "Images", list))
            counter1 += 1

        elif list.lower().endswith((".docx", ".doc", ".pdf", ".txt", ".xlsx", ".pptx")):
            shutil.move(file_path, os.path.join(user_input, "Documents", list))
            counter2 += 1

        elif list.lower().endswith((".mp4", ".avi", ".mkv", ".mov")):
            shutil.move(file_path, os.path.join(user_input, "Videos", list))
            counter3 += 1

        else:
            shutil.move(file_path, os.path.join(user_input, "Others", list))
            counter4 += 1

    print("\nFiles organized successfully!")
    print("Images:", counter1)
    print("Documents:", counter2)
    print("Videos:", counter3)
    print("Others:", counter4)

else:
    print("No file existing")
# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

major mistake i made was not checking if the user input path exists or is a directory before trying to create folders and move files.
This could lead to errors if the path is invalid. I added a check using os.path.exists

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
