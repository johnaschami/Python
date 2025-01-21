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


# While this works, it can be confusing if you plan to use the result later for calculations. Consider separating error messages from numeric results to avoid mixing data types.

    if num2 == 0:
        print("Error: You cannot divide by zero")
        result = None  # Assign None or handle error separately
    else:
        result = num1 / num2
else:
    print("Invalid operator")
    result = None  # Assign None if the operator is invalid


# 2. Temperature Converter (Easy)
# Create a program to: Convert a temperature from Fahrenheit to Celsius or vice versa. Ask the user which conversion they want (F to C or C to F) and then perform it.

# Step 1: Ask the user for the conversion type
conversion_type = input("Enter conversion type (F to C or C to F): ").strip()    # The .strip() method in Python is used to remove any leading and trailing whitespace (spaces, tabs, or newline characters) from a string.

# Step 2: Ask the user for the temperature value
temperature = float(input("Enter the temperature: "))

# Step 3: Perform the conversion
if conversion_type == "F to C":
    converted_temperature = (temperature - 32) * 5 / 9
    print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")
elif conversion_type == "C to F":
    converted_temperature = (temperature * 9 / 5) + 32
    print(f"{temperature}°C is equal to {converted_temperature:.2f}°F")
else:
    print("Invalid conversion type. Please enter 'F to C' or 'C to F'.")



# 3.  Basic Password Strength Checker (Medium)
# Write a program to: Take a password as input. Check if it’s strong by meeting these conditions: 1. At least 8 characters. 2. Contains both uppercase and lowercase letters. 3. Contains at least one number. And use conditional statements to give feedback (e.g., “Weak password: no numbers”).


password = input("What is your new password?: ")

if len(password) == 8:
    print("Voila")

# 4. Shopping Discount Calculator (Medium)
# Create a program that: Asks the user for the total amount of a purchase. Applies a discount based on these conditions: Purchases above $100 get a 10% discount. Purchases above $200 get a 20% discount. Print the discounted price.



