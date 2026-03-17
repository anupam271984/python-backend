### 👨‍💻 Implicit:
num_int = 10      # Integer
num_float = 5.5   # Float
result = num_int + num_float 
print(result)     # Output: 15.5
print(type(result)) # Output: <class 'float'>

### 👨‍💻 Explicit:
a = 1
print(type(a))
b = "1"
print(type(b))


# int(): Converts a value to an integer.
s = "100"
n = int(s)  # Converts string "100" to integer 100

# float(): Converts a value to a floating-point number.
n = 5
f = float(n)  # Converts integer 5 to float 5.0

# str(): Converts a value to a string.
age = 25
message = "I am " + str(age) + " years old." # Necessary for concatenation

# list(), tuple(), set(): Converts between collection types.
my_list = [1, 2, 2, 3]
my_set = set(my_list) # Result: {1, 2, 3} (removes duplicates)
