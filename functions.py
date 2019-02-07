# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
def sayHello():
    print("Hello to me")

# Create a functions with params
def saySomething(name = 'Sam'):
    """
    Prints Hello and then name
    """
    print('Hello ' + name)

# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total

# Call the function
sayHello()
saySomething('Mika')
total = getSum(1,2)
print(total)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# Creating a lambda
getSum = lambda num1, num2 : num1 + num2
print(getSum(101, 3))

addOneToNum = lambda num : num + 1
print(addOneToNum(100))

makeCacl = lambda num1, num2 : num1 * num2
print(makeCacl(101, 102))