fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry (negative indexing starts from the end)

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4]) # Output: (20, 30, 40) # slicing

colors = ("red", "green", "blue")
print(len(colors)) # Output: 3 # length

tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined = tuple1 + tuple2
print(combined) # Output: (1, 2, 3, 4, 5) # concatination , new tuple created

point = (10.5, 20.0) #Unpacking assigns the values of a tuple to individual variables in a single statement
x, y = point
print(f"X coordinate: {x}, Y coordinate: {y}")
# Output: X coordinate: 10.5, Y coordinate: 20.0

stars = ("*",) * 3 # Multiply a tuple by an integer using the * operator to repeat its content. 
print(stars) # Output: ('*', '*', '*')

# Example of Tuple Methods
my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Count how many times '7' appears
print(my_tuple.count(7))  # Output: 2

# Find the first index of the value '8'
print(my_tuple.index(8))  # Output: 3

# Example of a Nested Tuple
nested = (("A", "B"), (1, 2, 3), (True, False))

# Accessing the second tuple (index 1)
print(nested[1])          # Output: (1, 2, 3)

# Accessing the third element of the second tuple
print(nested[1][2])       # Output: 3

# Example of Iteration
fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(f"I like {fruit}")


# Example of Membership
colors = ("red", "blue", "green")

print("red" in colors)    # Output: True
print("yellow" in colors) # Output: False

#Since tuples are immutable, you cannot change them directly. To "update" one, you must temporarily convert it to a list, make your changes, and then convert it back into a tuple.
# 1. Original Tuple
coordinates = (10, 20, 30)

# 2. Convert to List
temp_list = list(coordinates)

# 3. Modify the List
temp_list[1] = 99  # Changing 20 to 99
temp_list.append(40) # Adding a new item

# 4. Convert back to Tuple
coordinates = tuple(temp_list)

print(coordinates) 
# Output: (10, 99, 30, 40)




