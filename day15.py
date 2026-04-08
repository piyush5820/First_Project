# Day 15: File Handling in Python

# File handling is the process of working with files on your computer.
# Python provides built-in functions to read from and write to files.

# Opening a file:
# open() function is used to open a file. It takes two arguments: filename and mode.
# Modes:
# 'r' - Read mode (default) - opens file for reading
# 'w' - Write mode - opens file for writing (overwrites existing content)
# 'a' - Append mode - opens file for appending (adds to existing content)
# 'x' - Exclusive creation - creates a new file, fails if file exists
# 'b' - Binary mode (can be combined with others, e.g., 'rb', 'wb')
# 't' - Text mode (default, can be combined with others)

# Example 1: Writing to a file
file = open('example.txt', 'w')
file.write("Hello, World!\n")
file.write("This is day 15 of Python learning.\n")
file.close()  # Always close the file after operations

# Better way using 'with' statement (automatically closes file):
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is day 15 of Python learning.\n")
print("File written successfully")

# Example 2: Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line:
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Reading all lines into a list:
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Example 3: Appending to a file
with open('example.txt', 'a') as file:
    file.write("Adding more content to the file.\n")

# Example 4: Working with binary files (like images)
with open('image.jpg', 'rb') as file:
    data = file.read()
    print(f"Read {len(data)} bytes")

# Example 5: Checking if file exists before operations
import os
if os.path.exists('example.txt'):
    print("File exists")
else:
    print("File does not exist")

# Example 6: Getting file information
import os
if os.path.exists('example.txt'):
    print(f"File size: {os.path.getsize('example.txt')} bytes")
    print(f"Last modified: {os.path.getmtime('example.txt')}")

# Example 7: Reading and writing CSV-like data
# Writing data:
with open('data.txt', 'w') as file:
    file.write("Name,Age,City\n")
    file.write("John,25,New York\n")
    file.write("Jane,30,London\n")

# Reading and processing data:
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:  # Skip header
        name, age, city = line.strip().split(',')
        print(f"{name} is {age} years old and lives in {city}")

# Example 8: Error handling with files
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")

# Example 9: Working with directories
import os
os.mkdir('new_directory')  # Create directory
os.chdir('new_directory')  # Change current directory
print(os.getcwd())  # Get current working directory
os.chdir('..')  # Go back to parent directory

# Example 10: Listing files in a directory
import os
files = os.listdir('.')
print("Files in current directory:")
for file in files:
    print(file)

# File handling is essential for many real-world applications like data processing,
# logging, configuration management, and more. Always remember to close files
# or use the 'with' statement to ensure proper resource management.