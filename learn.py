# Variables & Data Types

# A variable is a data container which helps us to store, manage and work with data. 

character_name = "John"
character_age = "35"

# working with STRINGS

print("HakunaMatata AI") # use \n to separate with lines or use \" to add a quoation mark or we can also create a variable with a string

print("HakunaMatata \n Lab")
print("HakunaMatata\"Lab")
phrase = "HakunaMatata AI"

print(phrase.upper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("AI"))
print(phrase.replace("AI", "Lab"))

# working with NUMBERS 

print(2)
print(-3.87)
print(3.6 )
print((3 + 23) * 444)
print(10 % 3) # modulus operator (giving the reminder of 10/3)

my_num = 8 
print(str(my_num))
print(pow(4, 6))
print(max(2, 6))
print(round(3.9))

# input
kaka = input("what is your name? ")
print("Hello brother " + kaka + " how are you doing?")


# LISTS []
# most of the time we will deal with a lot of data, so we need to find a way to manage and organize these data. List is one of the ways to achieve this. 

friends = ["Jerry", "Faustin", "Baraka"]
friends[2] = "Barakaaa"
lucky_numbers = [3, 7, 8, 14, 33, 40]

print(friends)
print(friends[0:1])

friends.extend(lucky_numbers)
friends.append("Chuwa")


#TUPLE ()
# they are immutable - can't be changed/modified 
# you when you wanna store data that can't be changed. 
coordinates = (4, 5)

# FUNCTIONS - a collection of code that perform a specific task. 

# we write a function that say hi to the user 
def say_hi():
    print("Hello User")

# to execute this function we just call it by name (you need to invoke/call the code - you store then reuse it)
say_hi()

# parameters & arguments (parameters are like handles and arguments are actual values you pass into them)
def say_hii(name, age):
    print("Hello " + name + ", you are " + age)

say_hii("Mike", "35")


def addtwo(ab, ba):
    added = ab + ba
    return added

x = addtwo(3, 5)
print(x)


# RETURN STATEMENT 
def cube(num):
    return num * num * num

cube(3)

# IF STATEMENT 
is_male = True
is_tall = True 

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")



# 4 PATTERNS OF CODE  
# Sequential # Conditional # Iteration # Store and Reuse (eg. functions)



# LOOPS AND ITERATIONS 

# we use WHILE as a keyword 
n = 5 

while n > 0 :
    print(n)
    n = n -1 
print('wow')

# Infinite Loop - doesn't end. To get out of the loop we use BREAK statement.  

# Definitive Loop

for i in [5, 4, 3, 2, 1]:
    print(i)
print('wow')

# iteration variable (looking for In) - moves through all of the values in the sequence
friends = ["Yoyo", "Yaya", "Yeye"]
for friend in friends:
    print("Happy New Year", friend)
print("Done")

# smart loop - finding the largest value 

largest_so_far = -1
print("Before", largest_so_far)
for the_num in [23, 4, 74, 12, 58]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("After", largest_so_far)


# Counting in a loop

zork = 0
print("Before", zork)
for thing in [2, 45, 78, 85, 45]:
    zork = zork + 1 
    print(zork, thing)
print("After", zork)

# Summing in Loop

zork = 0
print("Before", zork)
for thing in [34, 2, 56, 43, 67]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)


# finding the average in a loop

count = 0
sum = 0
print("Before", count, sum)
for value in [34, 23, 56, 12, 78]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)


# Filtering in a loop ( we use IF statement in the loop to filter)

print("Before")
for value in [34, 23, 56, 78, 12]:
    if value > 20:
        print("Large number", value)
print("After")


# Search using a Boolean Variable 

found = False
print("Before")
for value in [23, 45, 67, 43, 12]:
    if value == 43:
        found = True
    print(found, value)
print("After", found)


# Finding the smallest value

smallest = None
print("Before")
for value in [9, 43, 4, 23, 67]:
    if smallest is None:
        smallest = value 
    elif value < smallest:
        smallest = value 
    print(smallest, value)
print("After", smallest)





