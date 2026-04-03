# Definition
def greet():
    print("Hello from a function!")

# Calling the function
greet() 
#-------------------------------#

def addition(a,b):
    c = a+b
    print("addition is ",c)

a = 10
b = 20
addition(a,b)    
#-------------------------------#
def get_personaname(name):
    print(f"Hello, {name}!")

    
    get_personaname("AP") # this will not work due to indented rule

#-----------------------------------------#
def greet_person(name):
    print(f"Hello, {name}!")

# To run it:
greet_person("Alex") # this will  work due to indented rule

# 1. Returning without Parameters
#This function generates a piece of data and "hands it back" to the code that called it. 

def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns an integer."""
    return a + b

result = add_numbers(10, 5)
print(result)  # Output: 15
#-----------------------------------------#
def multiple(e,f):
    g = e*f
    print(f"this value of multiplication is, {g}")

multiple(3,4)   

#--------------------------------------------#
#1. Positional Arguments
def greet(name, age):
    print(f"Hello {name}, your {age} years old")

greet("Rahul", 30)
#--------------------------------------------#
#2. Keyword Arguments : You can pass arguments by explicitly naming the parameter. This means the order doesn't matter.\

def describe_pet(animal_type , pet_name):
    print(f"i have a {animal_type }, named {pet_name}")

describe_pet(pet_name="ronny", animal_type="dog")    # order doesn't matter
describe_pet(animal_type="dog" ,pet_name="ronny")    

#--------------------------------------------#
#3. Default Arguments :You can provide a default value in the function definition. If the caller skips that argument, the default is used.
def power(number, exponent=2):
    return number ** exponent

print(power(4))      # Uses default: 16 (4^2)
print(power(4, 3))   # Overrides default: 64 (4^3)

#-----------------------------------------------#
#4. Arbitrary Arguments (*args and **kwargs)
'''When you don't know how many arguments will be passed, use these:
*args: Receives a tuple of positional arguments.
**kwargs: Receives a dictionary of keyword arguments.
'''
def pizzaMaking(size , *pizza):
    print(f"I made {size} {pizza}")    
pizzaMaking("large", "wheat pizza","musroom","extra cheese")   

def emailItems(recipient, subject, body):
    print(f"To: {recipient}, Subject: {subject}, sender: {body}")

email_info = {
    "recipient": "test@example.com",
    "subject": "Hello!",
    "body": "This is a test message."
}
emailItems(**email_info) #To: test@example.com, Subject: Hello!, sender: This is a test message.
