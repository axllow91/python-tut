# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


# Core modules (packages)
import datetime
from datetime import date
import time
from time import time

# Pip modules
import camelcase

# Custom module import (validator.py)
import validator
from validator import validate_email

today = datetime.date.today()
print(today)

# using the from datetime import date
day = date.today()
print(day)

# time
timestamp = time()
print(timestamp)

# Camelcase
camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))

# Using the custom import (validator)
email = 'test@test.com'
if validator.validate_email(email):
    print(f'{email} is valid')
else:
    print(f'{email} is not valid')

# Using the custom import with the actual function
email1 = 'test@smth.com'
if validate_email(email1):
    print(f'{email1} is valid')
else:
    print(f'{email1} is not valid')