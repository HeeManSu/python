# Key value pairs in python

marks = {'Hindi': 89, 'English': 90}

print(type(marks))

print(marks['English'])
print(marks.get('Hindi'))

# To add an key value pair
marks['Maths'] = 100
print(marks['Maths'])

# Delete value from a dictionary
del marks['English']
print(marks)


# To get length
print(len(marks))