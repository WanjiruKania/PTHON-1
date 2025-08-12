my_list = []
# append items to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert a value 
my_list.insert(1 , 15)

# extend the list with another list
another_list = (50, 60, 70)
my_list.extend(another_list)

# remove an item from the list
my_list.pop()

# sort the list in an ascending order
my_list.sort()

# find an print the inex of a value
index_of_30 = my_list.index(30)
print(index_of_30)