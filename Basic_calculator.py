number1 = input("Enter a number: ")
number2 = input("Enter another number: ")

number1 = float(number1)   # we used FLOAT because we want our users to be able to use both decimals and whole numbers
number2 = float(number2)

result = number1 + number2

print(result)


# we can also try to change European stair no to US floor number 

inp = input("What is the number of the floor? ")
ufl = int(inp) + 1
print("US Floor", ufl)

