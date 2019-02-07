# Python has functions for creating, reading, updating, and deleting files.

# Open File
# We can open a file that does not exist; it will be created automatically
myFile = open('myfile.txt', 'w') # w for writting

# Get info
print('Name: ', myFile.name)
print('Is Closed? ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write something to file
myFile.write('I love Python!')
myFile.write('\nAnd I love Java')
myFile.write('\nAnd I love Javascript')
myFile.write('\nAnd I love C++')

# Close file after we finished writting on it
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a') # a is for append something into file
myFile.write(' I also like Typescript')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+') # r+ for reding from the file
n_chars = 100 # max chars to read from the file
text = myFile.read(n_chars) # reading the first 10 char
print(text)









