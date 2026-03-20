# The capitalize() method transforms the first character of a string to uppercase and converts all other characters to lowercase

text = "python is FUN!"
print(text.capitalize())  # Output: "Python is fun!"

# title() If you need to capitalize the first letter of every word in a string, use the title() method

text = "hello world"
print(text.title())  # Output: "Hello World"

# Sometimes you need more control, such as capitalizing the first letter without forcing the rest of the string into lowercase.
# Slicing and upper(): This keeps the case of the remaining characters intact

text = "pYTHON"
# Capitalize first letter, keep the rest as is
result = text[:1].upper() + text[1:] 
print(result)  # Output: "PYTHON"

# Upper() entire string uppercase
text1 = 'this is noida'
print(text1.upper())

# The .center() method is used to align a string in the middle of a specified width by adding padding characters (usually spaces) to both sides
text = "Python"
print(text.center(20))
# Output: '       Python       '

text = "CHAPTER 1"
print(text.center(30, "-"))
# Output: '----------CHAPTER 1-----------'
# Immutability: Like all string methods, it returns a new string and doesn't change the original.

text1 = "CHAPTER 1"
print(text1.center(12, "-"))
# Output: '-CHAPTER 1--'

# The .count() method is used to find out how many times a specific substring appears within a larger string. It is case-sensitive and does not count overlapping characters
text = "apple pie"
print(text.count("p")) 
# Output: 3

text = "banana"
print(text.count("ana")) 
# Output: 1

text2 =['ab', 'cd', 'cd', 'ab', 'ff']
print(text2.count('cd'))
# Output: 2

# find(): The Explorer
# This searches for a substring and returns the index (position) of its first occurrence
phrase = "Hello Python"
print(phrase.find("Py"))  # Output: 6
print(phrase.find("Java")) # Output: -1

# index(): The Strict Finder
# This works exactly like find(), but with one major difference: if the text isn't found, it raises a ValueError and stops your program.
phrase = "Hello Python"
print(phrase.index("Py"))  # Output: 6
# print(phrase.index("Java")) # Raises ValueError: substring not found
