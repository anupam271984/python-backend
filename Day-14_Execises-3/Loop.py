for i in range(1, 5):
    print(i)
# How many times loop will run

nums = [10, 20, 30]
total = 0
for x in nums:
    if x > 15:
        total += x
print(f" the value of total is {total}")


for i in range(0, 6, 2): #range(start, stop, step)
    print(i, end=" ")
