## Basically a js object. key value pairs, 

my_dict = {
    "name": "sam",
    "age" : 25,
    "dogs" : ('Charlie, Darcy')
}

# we only have bracket notation

print(my_dict["name"]) # sam

my_dict['dogs'] = ['Charlie', 'Darcy', 'Tulip'] # changed dogs from tuple to list


# add a new field to a dict
my_dict.update({"hobbies" : ['Reading', 'Drawing']})

# or like this 

my_dict['fav_number'] = 'blue'
print(my_dict)

for x in my_dict:
    print(my_dict[x])