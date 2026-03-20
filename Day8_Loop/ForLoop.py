for i in range(5):
    print(f"Iteration {i}")


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I love {fruit}!")

for n in range(1, 10):
    if n == 5:
        continue  # Skip the number 5
    print(n)


characters =["AS", "BS", "DS", "SADFEW"]
for char in characters:
    print(char)
    for i in char:
        print(i)

num = 123444455
for i in num:
    print(i)  # Error int is not iterable