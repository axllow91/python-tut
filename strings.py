# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'MEYOU2'
age = 99

# Concatenate 
print('Hello to ' + name + ' who is ' + str(age))

# String Formatting

# Arguments by positions
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c')) # will change the printing positioning b becomes first, c second, a last

# Arguments by name
print('My name is {name} and I am {age} years old'.format(name=name, age=age))

 # F-Strings (only py 3.6+) which is much easier
print(f'My name is {name} and I am {age} years old')

# String Methods

s = 'Hello there and here'

# Capitalize first letter
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Swap case makes first letter (if is uppercase) lower case and vice-versa
print(s.swapcase())

# Get lenght of a string
print(len(s))

# Replace 
print(s.replace('there', 'runawa'))

# Count the letter found in the string
sub = 'e'
print(s.count(sub))

# Starts with
print(s.startswith('hello')) # false

# Ends with
print(s.endswith('e')) # true

# Split the string into a list
print(s.split())

# Find position
print(s.find('r'))



