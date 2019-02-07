# If/ Else conditions are used to decide to do something based on something being true or false
x = 5
y = 6

# Simple if
if x < y:
    print(f'{x} is not greater than {y}')


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
if x == y:
    print('They are equal')
elif x != y:
    print('They are not equal!')
else:
    print('Some variable is greater then another')

# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} < 10')


# Logical operators (and, or, not) - Used to combine conditional statements
if x > y and x > 3:  # AND operator
    print('I found that nothing is unreal')


if x > y or y < 10:  # or operator
    print('Something happend')
else:
    print('We done something wrong')

# not
if not(x == y):
    print(f'{x} is not equal {y}')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1, 2, 3, 4, 5, 6]

# in
# if x in numbers:
#     print(x in numbers)  # true 5 is in list numbers

if x not in numbers:
    print(x in numbers) # false 5 is in numbers

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
a = 23
b = 53

# is
if a is b: 
    print(a is b) # true

# is not
if a is not b:
    print(a is not b) # true