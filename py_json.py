# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# Sample JSON (this usually will come from an APi)
userJSON = '{"first_name": "John",' \
    '"last_name": "Doe",' \
    '"age": 30}'

# Parsing to dictionary
print('Parsing from JSON to dictionary...')
user = json.loads(userJSON)
print(user)

# dictionary (which means is an object)
car = {'make': 'Ford', 'model': 'Ferrari', 'year': 1970}

# Searialize an object to a JSON format
carJSON = json.dumps(car)
# printing in a json format
print(carJSON)