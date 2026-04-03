# Single or Double Quotes :Most common for simple, single-line text.
name = 'Alice'
city = "New York"
print(name)
print(city)

# Triple Quotes (''' or """) : Used for multi-line strings or text that contains both single and double quotes.
message = """This is a 
multi-line string."""
print(message)

message1 = '''This is a 
multi-line string.'''
print(message1)

# F-Strings (Formatted Strings) : Preferred for embedding variables or expressions directly into text.
age = 25
print(f"I am {age} years old.") # Output: I am 25 years old.

# Raw Strings (r""): Useful for file paths or regular expressions because they ignore escape characters like \n.
path = r"C:\users\documents"
print(path)

# Concatenation (+): Joining two or more strings.
full_name = "John" + " " + "Doe" # Result: "John Doe"
print(full_name)

# Repetition (*): Repeating a string multiple times.
laugh = "ha" * 3 # Result: "hahaha"
print(laugh)

# Indexing and Slicing: Accessing specific characters or parts of a string.
text = "Python"
print(text[0])   # Output: 'P' (First character)
print(text[0:7]) # Output: 'Py' (Characters from index 0 to 1)

# Simple Iteration: Access each character directly
word = "Python"
for char in word:
    print(char)  # Prints P, y, t, h, o, n on separate lines

# Using enumerate(): If you need both the index (position) and the character.
for index, char in enumerate("Hi"):
    print(f"Index {index} has character {char}")

# Reverse Iteration: Use the reversed() function to loop backwards.
for char in reversed("Loop"):
    print(char) # p, o, o, L


    


