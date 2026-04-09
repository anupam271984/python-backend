'''print("Value: " + 10) # Error 

print("Value: " + str(10)) #Error'''

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
print(type(f"{2 * 30}"))

price1 = 49.09999
txt1 = f"For only {price:.3f} dollars!"
print(txt1)
