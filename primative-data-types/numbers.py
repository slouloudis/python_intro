''' Python Numbers '''

# There are three types of numbers in python

# These are all 'integers' - whole numbers

x = 4
y = -99
z = 0

# These are all floats - floating point numbers

a = 5.0
b = -77.2
c = 0.  # 0.0

# there is also a complex number type. something to do with imaginary numbers and square roots. but programmers stole i for making loops so we use j in python. 

you_have_to_be_smart_to_understand_this = 42j
print(f" {type(you_have_to_be_smart_to_understand_this)}, is really complex")

# Maths is possible. Most of what we do in js works the same here.


# Use ()'s to guarantee order as usual.

# you can do arithmatic with floats and ints with no issues, but the result will always be of type float

# if you use division, no matter if both numbers are ints, the result will be a float

my_cool_number = 5 / 5 # 1.0
print(f"{my_cool_number} is {type(my_cool_number)}") 

# unless you know the 'integer division operator'
my_cooler_number = 5 // 5 # 1

# Python has some nice built in functions for numbers

min(3 ,1 ,2) #1
max(100, 0, 5) # 100
round(3.1) # 3
round(5.9) # 6
round(5.78, 1) # takes an optional second argument for no. digitals -> 5.8 is result

# for more advanced stuff python offers a math module in the standard library.

# we can't do i++ or i--
x++ 
x--

# but this is fine
x += 1
x -= 1