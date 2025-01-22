names = ['Sam', 'Manny', 'Frankie']

# no length property, use len() method

len(names) # 3

# lists are 0 indexed. 
# can update index same as in JS

names[2] = 'Joe'

# we cannot assign to an index that is greater then the length of the array (doesn't exist)

# names[10000] = 'Tim' # Error: list assignment index out of range

numbers = [100, 23, 341, 3]

sorted_numbers = sorted(numbers) # returns sorted list, original is not changed
sorted_decending = sorted(numbers, reverse=True)
print(sorted_decending)

# numbers.sort() # changes orignal array
# numbers.sort(reverse=True)


# reverse (in-place)

numbers.reverse()

# push 

names.append('Angelica')

# can use extend to merge two lists in-place 
print(names.extend(numbers)) # None
print(names) # ['Sam', 'Manny', 'Joe', 'Angelica', 3, 341, 23, 100]

names.insert(4, 'Jez') # inserts Jez at index 4 and shuffles other element up by one

print(names)