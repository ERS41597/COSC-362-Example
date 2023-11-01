"""
Simple python script to demonstate Cloud 9 Terminal
"""

# Get name
name = input("What is your name?")

# Get birth year
birth_year = input("What year were you born?")

# Compute age
current_year = 2023
age = current_year - int(birth_year)

# Output
print(f"Hello, {name}!")
print(f"You are {age} years old.")
