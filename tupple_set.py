my_set = {1, 2, 3, 4, 5, 2}  # Sets automatically remove duplicates
print(my_set)
my_set.add(6)  # Adding an element to the set
print(my_set)
print(len(my_set))  # Length of the set
# my_set.remove(3)  # Removing an element from the set

for element in my_set:  # Iterating through the set
    print(element)


# print(my_set[0])  # Sets do not support indexing
print(2 in my_set)  # Checking if an element is in the set
my_set.discard(2)  # Removing an element from the set without raising an error if it does not exist
print(my_set)

# tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0])  # Accessing the first element
print(len(my_tuple))  # Length of the tuple
# my_tuple[0] = 10  # Tuples are immutable, this will raise an error
print(my_tuple[1:4])  # Slicing the tuple
# my_tuple.append(6)  # Tuples do not support appending, this will raise an error


