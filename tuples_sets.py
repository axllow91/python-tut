# A Tuple is a collection which is ordered and unchangeable (at the compile the order cannot change). Allows duplicate members. 
# You can't delete idividual elements from a tuple but you can delete the whole tuple


# Simple turple
fruit_tuple = ('Orange', 'Mango', 'Apple')
print(fruit_tuple)

# Using constructor
fruit_tuple_c = tuple(('Apple', 'Orange', 'Mango'))
print(fruit_tuple_c)

# Can not change value in a tuple (ERROR)
# fruit_tuple[1] = 'Grape' # error: fruit_tuple does not support item assignment
# print(fruit_tuple)

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)


# Get the length of tuple
print(len(fruit_tuple))

# Can't delete a single element from a tuple but YOU CAN DELETE the whole tuple
# so...
del fruit_tuple_2
# print(fruit_tuple_2) # NameError: name 'fruit_tuple_2' is not defined does not exist anymore


# A Set is a collection which is unordered and unindexed (at compiling the indexing can/will change). No duplicate members. Curly braces for sets
# If a duplicate item exist inside of a set it will be ignored by the compiler
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}
print(fruit_set)

# Check if in set (check if element exist in set)
print('Apples' in fruit_set)

# Add to set
fruit_set.add('Grape')
print(fruit_set)

# Remove from set
fruit_set.remove('Grape')
print(fruit_set)

# Clear set
fruit_set.clear()
print(fruit_set) # set() means is empty and we can add elements

# Delete set
del fruit_set