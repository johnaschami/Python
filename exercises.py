# 1. Simple Calculator (Easy) 
# Write a program that: Asks the user to input two numbers and an operation (+, -, *, /). Performs the operation and prints the result. Use conditional statements to handle invalid operators.

# Step 1: Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Step 2: Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operator"

# Step 3: Display the result
print("Result:", result)



# 2. Temperature Converter (Easy)
# Create a program to: Convert a temperature from Fahrenheit to Celsius or vice versa. Ask the user which conversion they want (F to C or C to F) and then perform it.







