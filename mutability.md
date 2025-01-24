Mutable (changeable in place): Their contents can be modified after creation.
Immutable (unchangeable): Once created, their contents cannot be changed, without creating a new memory adress with a new value.

strings are immutable -> when we 'change' them we're kinda just making a new string. This is a performance concern in python. 

In Python:

Immutable types (str, tuple, int) create new objects when changed.
Mutable types (list, dict) modify in place and affect all references.
Be careful with mutable default arguments in functions!


In JavaScript:
Primitives (string, number) are passed by value.
Objects and arrays are passed by reference, meaning modifications affect the original object.
Use const to prevent unintended changes, but it still allows modifying object contents.

Actually this kinda leads into why useState is the way it is.