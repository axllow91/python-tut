# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# x = 1  # integer
# y = 2.5 # floating-point number
# name = 'Brad' # string
# is_cool = True # boolean (booleans needs to be upper case)

# Multiple assignments
x, y, name, is_cool = (1, 2.5, 'Me', True) # shorthand for what we did upper
print(x, y, name, is_cool)

print(type(is_cool)) # getting the type of variable is_cool

# Casting from double to int
y = (int(2.5))
print(y)

# Casting from int to string
x = str(x)
print(type(x)) # get the type of variable x

# Casting from int to float
x = float(x)
print(x) # decimal number