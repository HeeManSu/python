# Similar to array in java. 


user_list = ['Ram', 'Himanshu', 'Kinshu', 'Anshu', 'Sham']
print(user_list[0])
print(user_list[1])


user_list.append('Paul')   # add at the end of the list.
print(user_list)


user_list.remove('Himanshu')
print(user_list)


user_list[0] = 'Rama'
print(user_list)


user_list.insert(1, 'Shyam')
print(user_list)

del user_list[3]
print(user_list)

# Total number of items in a list
print(len(user_list))

# Sorting the items in list

user_list.sort()
print(user_list)

# Reverse sorting
user_list.sort(reverse= True)
print(user_list)


# To reverse the list

user_list.reverse();
print(user_list)

# Popping items in list. 
# Removes items in the end. 

print(user_list.pop());
print(user_list.pop(2));



# Slicing of list. 

# First two items
print(user_list[0:2])

# Middle 3 items
print(user_list[1:3])

# Last 2 items
print(user_list[-2:])


#Max , Min and Sum in a list. 

marks = [20, 39, 23, 60, 78,]
print(min(marks))
print(max(marks))

print(sum(marks))


# Mix List

mix_list = ['Paul', 23, 34.3, True]