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

# to execute this function we just call it by name 
say_hi()

# parameters & arguments 
def say_hii(name, age):
    print("Hello " + name + ", you are " + age)

say_hii("Mike", "35")

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






