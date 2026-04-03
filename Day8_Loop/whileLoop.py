count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # Crucial! If you don't update this, the loop runs forever.

#Sometimes you want a loop to run until a specific event happens inside the code. We use while True combined with a break statement.
while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == "exit":
        break  # This immediately stops the loop
    print(f"You typed: {user_input}")

# Just like in for loops, continue skips the rest of the current block and jumps back to the top to check the condition again.

n = 0
while n < 6:
    n += 1
    if n == 3:
        continue  # Skips printing '3'
    print(n)

# The Python "Do-While" Pattern
#Instead of putting the condition at the top, you put it inside an if statement at the end of the loop.
while True:
    # 1. This code runs AT LEAST once
    password = input("Enter password: ")
    
    # 2. Check the condition at the bottom
    if len(password) >= 8:
        break  # Exit the loop if condition is met
    
    print("Error: Password must be 8 characters.")


'''while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break'''
