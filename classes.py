# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it.
#  Almost everything in Python is an object


class User:
    # Constructor
    # self is similar to this in java (mandatory to be passed on constructor when created, first in order)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        # using similar like this.name in java or typescript, javascript
        return f'My name is {self.name} and I am {self.age} years old'

    def has_birthday(self):
        self.age += 1


# Initialize user object
me = User('Marian', 'me@mailme.com', 101)
girldUser = User('Daniela', 'daniela@waileo.com', 50)
print('Creating new User...')
print('User: ' + me.name + '\n' + 'Email: ' +
      me.email + '\n' + 'Age: ' + str(me.age))


# Edit property
myAge = me.age = 70
print(myAge)

girldUser.has_birthday()

# calling the greeting method one the user
print(girldUser.greeting())


# Customer class
class Customer:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        if self.balance == 0:
            print(
                f'Customers {self.name} balance is empty: ' + str(self.balance))

        return self.balance

    # toString() method equivalent in Python
    def __str__(self):
        return 'Name:' + self.name + '\nEmail: ' + self.email + '\nAge: ' \
            + str(self.age) + '\nBalance: ' + str(self.get_balance())


# Initialize Customer Object
john = Customer('John Wick', 'johnw@best.com', 50)
print('-----------------------------------------')
print(john)  # getting the to string __str__() methond
john.balance = 500
print(john)
