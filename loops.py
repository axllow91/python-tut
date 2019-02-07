# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Wick', 'Don', 'Maseria', 'Alberta']
for person in people:
    print('Current person: ', person)

print('-----------------------------------')

# Break out
for person in people:
    print('Current person: ', person)
    if person == 'Maseria':
        break

print('-----------------------------------')

# Continue - that means one variable is skipped
for person in people:
    if person == 'Don': 
        continue # Don is skipped
    print('Current person: ', person)

print('-----------------------------------')

# Range simple example
for i in range(0, 10):
    print('Number ', i)

# range within person list
for i in range(len(people)):
    print('Current person ', people[i])

# While loops execute a set of statements as long as a condition is true.
count = 0

# infinite loop
#while cout < 5:
#   print('You are in a infinite loop')

while count <= 10:
    print('Count: ', count)
    count += 1


# finite loop
x = 5
while x >= 0: # lopped 6 times (if > loopped 5 times)
    print('You are in a finite loop')
    x -= 1


