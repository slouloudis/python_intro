# strings in python can be written with ''`s or ""`s

greeting = "Hello"

# can use a backslash to escape
'It\'s Sam'

# or
"It's Sam"

# we can use print to print. We can use f-strings (template literals) - only work with ""'s

print(f"{greeting}, sam")

# concatination works

greeting + "sam"

# python doesn't do type coercion, so the below doesn't work
# print(2 + '2')


# ------ String Methods -------

# you can call dir(str) to see all string methods
# and help(str.title) to see a helpful message about what it does

# doesnt replace in-place
x = 'sam rulezz'
print(x)
y = x.replace('rulezz', 'droolzz')
print(x)
print(y)


# some string methods that exist in python but not in JS 

'hello'.count('l') # 2 because two ls in hello. Can provide more arguments for index to start search and index to end. 
ws = 'wow this wonderous weather wearily waves'.count('w', 0, 10) # 3


'Whatever'.swapcase() # wHATEVER 

# first argument is the total length of the string, not just how much padding you want on either side. nice is 4x, then I add '--' on either side with the remaining 4 spaces
# annoying
x = 'nice'.center(8, '-')
print(x)

my_dogs = 'Charlie, Darcy, Einstien'

print('Charlie' in my_dogs) # True
print('Coco' in my_dogs) # False