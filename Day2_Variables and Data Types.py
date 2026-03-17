# Variables and Data Types
#------------------------------------------------------------------------
# 1. Numeric data: int, float, complex
int1 = 3
int2 = -8
int3 = 0
float1 = 7.349 
float2 =-9.0 
float3 = 0.0000001
complex1 = 6 + 2j
print(int1)
print(float1)
print(f"The complex number is: {complex1}")
print(f"Real part: {complex1.real}")
print(f"Imaginary part: {complex1.imag}")
#------------------------------------------------------------------------

# List
badges = ["Admin", "Architect", "Developer"]
print(badges)

#------------------------------------------------------------------------
# Dictionary
user = {"name": "Amit", "points": 50000}
print(user)

#------------------------------------------------------------------------
#tuple = Used for data that cannot change (Immutable). It’s like a "Read-Only List
coordinates = (12.97, 77.59)
print(coordinates)

#------------------------------------------------------------------------
name = "Trailblazer"  # String 
badges = 50           # Integer
is_certified = True   # Boolean 

# F-Strings: The modern way to combine text and variables
print(f"User {name} has {badges} badges. Certified: {is_certified}")

# If i need to print each statement in new line then add \n
print(f"User {name}\nhas {badges} badges.\nCertified: {is_certified}")

a = 1
print(type(a))
b = "1"
print(type(b))
