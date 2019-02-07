# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dictionary
person = {
    'first_name': 'John',
    'last_name': 'Wick',
    'age': 33
}

print(person)

# Using a constructor
person_cons = dict(first_name = 'John', last_name = 'NotWeak',age = 30)
print(person_cons)

# Access a single value (2 methods to do it)
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-555-5555'

# Get keys
print('Keys: ' + str(person.keys()))

# Get values
print('Items: ' + str(person.items()))

# Make a copy 
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# Remove item (2 methods)
del(person['age'])
person.pop('phone')
print(person)

# Clear 
person.clear()
print(person) # {} 

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 40},
    {'name': 'Aertha', 'age': 129}
]
# printing the first dictionary
print(people[0])
# printing the second dictionary with only the name
print(people[1]['name'])

# Delete dictionary
del(person)
# print(person) # NameError: name 'person' is not defined



