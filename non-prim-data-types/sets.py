# sets are cool - like a list but you cannot have duplicates, and they store immutable data types  - very fast, and some uniqe methods like 'union' 

my_set = {2, 3}

my_set2 = {3,3,4} # the actual set will be {3,4} because we cannot have duplicates

list_of_names = ['Sam', 'Sam', 'Angelica']

unique_names = set(list_of_names) # ['Sam', 'Angelica']

# sets dont have an order 

print(unique_names)

#print(unique_names[0]) # error 'set' object is not subscriptable

unique_names.add('Frankie')

unique_names.discard('Sam')