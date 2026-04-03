# creating a list
fruits =["Apple", "Mango","Guava","Banana"]

# accessing a list value
print(f"The list has {fruits[0]} in first place")
print(f"The list has {fruits[3]} in lasts place")
print(f"The list has {fruits[-1]} in last place") # negative index

# methods
print(f"Length of list is {len(fruits)}") # length : len

fruits.append("Orange")
print(f"New appended list is {fruits}") # append : adding items in end of list

fruits.insert(2, "Grapes")
print(f"The new item in 3rd Postion is Graped in new {fruits} list") #insert : adding new item in specific postion

fruits.insert(4, "Banana")
print(f"new list fter banana instered is : {fruits}") #new list: ['Apple', 'Banana', 'Grapes', 'Guava', 'Banana', 'Mango', 'orange']  

fruits.remove("Banana")
print(f"new list after banana reoved is : {fruits}") # new list: : ['Apple', 'Grapes', 'Guava', 'Banana', 'Mango', 'orange']

newFruits =["WaterMelon", "Kiwi"]
fruits.extend(newFruits)
print(f"new list after new fruits added is :{fruits}")

fruits.sort()
print(f"new sorted list {fruits}")

fruits.pop()
print(f" new list after pop {fruits}")  #new list after pop ['Apple', 'Banana', 'Grapes', 'Guava', 'Kiwi', 'Mango', 'Orange']
# Removes and returns the item at a given index (default is last).

fruits.pop(1)
print(f" new list after popss 1s {fruits}")
# new list after popss 1s ['Apple', 'Grapes', 'Guava', 'Kiwi', 'Mango', 'Orange']

fruits.reverse()
print(f" new list after reverse {fruits}") # ['Orange', 'Mango', 'Kiwi', 'Guava', 'Grapes', 'Apple']

print(fruits.count("Apple"))  # Output: 1
print(fruits.count("Orange")) # Output: 1 
print(fruits.count("Watermelon")) # Output: 0
print(fruits.count("apple"))  # Output: 0 case sensitiive
numbers = [1, 2, 5, 2, 8, 2]
print(numbers.count(2))       # Output: 3

# check if else in list
if "Apple" in fruits:
    print(f"1An Apple a day keep doc away")
else:
    print(f"Buy an Apple")



