# 2. Variables and Data Types
name = "Trailblazer"  # String 
badges = 50           # Integer
is_certified = True   # Boolean 

# F-Strings: The modern way to combine text and variables
print(f"User {name} has {badges} badges. Certified: {is_certified}")

# If i need to print each statement in new line then add \n
print(f"User {name}\nhas {badges} badges.\nCertified: {is_certified}")

# List
badges = ["Admin", "Architect", "Developer"]
print(badges)

# Dictionary
user = {"name": "Amit", "points": 50000}
print(user)

#tuple = Used for data that cannot change (Immutable). It’s like a "Read-Only List
coordinates = (12.97, 77.59)
print(coordinates)