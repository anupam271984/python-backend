a = "Harry"
b = 'Apply'
c = "MY NAME IS ANTHONY GONSALVES"
d = "1"
e = ""

# length
print(len(a))
print(len(b))

# upercase - convert in upper case

print(a.upper())
print(d.upper()) # will not convert anser will be 1

# lowercase - conver in lower case

print(c.lower())
print(d.lower()) # will not convert anser will be 1

# strip() method is a built-in string function used to remove leading (start) and trailing (end) characters from a string
text = "555Hello Python555"
print(text.strip("5"))  # Output: "Hello Python"

text1 = "www.example.com"
# Removes any of 'w', '.', 'c', 'o', or 'm' from the ends
print(text1.strip("w.com"))  # Output: "example"

line = "Data processing is fun!\n"
print(line.strip())  # Output: "Data processing is fun!"

white = "   remove left right white spaces    "
print(white.strip())

# lstrip() (Left Strip)
#This method focuses exclusively on the beginning of the string. 
# Default: Removes leading whitespace (spaces, tabs, newlines).
text3 = "---Important---"
print(text3.lstrip("-"))  # Output: "Important---"

# rstrip() (Right Strip)
# This method focuses exclusively on the end  of the string. 
# Default: Removes trailing whitespace (spaces, tabs, newlines).
text4 = "---Important---"
print(text4.rstrip("-"))  # Output: "Important---"

# replace() : replace() method replaces all occurences of a string with another string.
text5 = "I like apples, apples are great."
print(text5.replace("apples", "bananas")) 
# Output: "I like bananas, bananas are great."
text6 = "i like salesforce , salesforce is wonderful product"
print(text6.replace("salesforce","python"))

#split:The split() method is the opposite of joining strings—it breaks a string into a list based on a specified separator
text = "Python is   awesome"
print(text.split())  # Output: ['Python', 'is', 'awesome']
# Note: It automatically handles multiple spaces as a single separator.

data = "apple,banana,cherry"
print(data.split(","))  # Output: ['apple', 'banana', 'cherry']

email = "user@mail.com@server"
print(email.split("@", 1))  # Output: ['user', 'mail.com@server']

email1 = "user@mail.com@server"
print(email1.split("@", 2))  # Output: ['user', 'mail.com@server']

