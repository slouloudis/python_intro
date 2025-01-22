# like this

def func_name(param = 'rainy'):
    # this is the func body
    # anything indented is considered part of the func body
    if param == 'sunny':
        print('its sunny')
        # also there are no ==='s in python. basically don't compare different data types (unless int & float)
    elif param == 'rainy': 
        print('its rainy')
    else: 
        print('idk what weather that is')

func_name('sunny')

func_name() 