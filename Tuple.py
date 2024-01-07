
#similar to list but you can't modify the items of Tuple.

# Immutable
# Ordered 

days = ('Mon', 'tues', 'wed', 'Mon')
print(type(days))
print(days)
print(days[1])


# Difference
days[1] = 'Sat'  # Not allowed

print(days.count('Mon'))  # How many times Mon came in the tuple
print(days.index('tues')) # What is the index of tues