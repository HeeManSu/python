# Similar to list but it is unordered

# Unordered and unique elements
# Unordered meand postion of element won't be same at the time of printing. 
# remove duplicated and prints only unique elements.

my_set = {'mon', 'tues', 'thrus'}
print(type(my_set))
print(my_set)


# Converting list into set

my_list = ['Mon', 'Tues', 'Wed', 'Thrus', 'Fri', 'Mon', 'Tues']
days_set = set(my_list)
print(days_set)