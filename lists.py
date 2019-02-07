# A List is a collection which is ordered and changeable. Allows duplicate members.

# Initiate a list in python
numbers = [1,2,3,4,5]
print(type(numbers))
print(numbers)

# Create list using a constructor
numbersList = list((1,2,3,4,5,6))
print(numbersList) 

# Creating a list with multiple types (will not throw error magic! until you want to sort because is not supported between instances(int and str))
'''12'''
fruits = ['Apples', 'Bananas', 'Pears', 'Oranges']
print(fruits[2])

# Get the lenght of the list
print(len(fruits))

# Append variables to the list (added at the end of the list)
fruits.append('Mangos')
print(fruits)

# Remove element from list
fruits.remove('Pears')
print(fruits)

# Insert element into list at the specific position
fruits.insert(2, 'Pears')
print(fruits)

# Remove from a specific position
fruits.pop(2)
print(fruits)

# Reverse list beginning gets to the end and the end is the beginning of list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse the sort
fruits.sort(reverse=True)
print(fruits)
