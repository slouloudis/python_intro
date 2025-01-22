# scope basically works the same, but if you want to modify a global var in a function you have to make it explicit 

x = 10

def change_x():
    x = 20
    print(x) # 20

change_x()
print(x) # still 10 (︶︹︶)

important_state_var = 'eyoo'

def change_important_state_var():
    # cant do in two lines as python considers them seperate statements
    # idk if good practice
    global important_state_var 
    important_state_var = 'ooye'

change_important_state_var()
print(important_state_var) # ooye