
# tuples are non-mutable lists

# list = [] - ordered and changeable
# tuple = () - ordered and unchangeld. duplicates ok. Faster (!?) optimisation stuff

info = ('sam', 25, ['charlie', 'darcy', 'tulip'], 'peach', 'peach tea')

print('sam' in info) # True
print(info.index(25)) # 1

print(info.count('peach')) # 1

for elem in info:
    print(elem)

# info[4] = 'something else' # 'tuple' object does not support item assignment

# info.append('Sam') # 'tuple' object has no attribute 'append'

numbers_tuple = (1,3,4)
# sorted returns a new list so we good (but not a tuple)
x = sorted(numbers_tuple)

# numbers_tuple.sort() # 'tuple' object has no attribute 'sort'
print(x)