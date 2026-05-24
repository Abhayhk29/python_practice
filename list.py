my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[0])  # Accessing the first element
print(len(my_list))  # Length of the list
my_list.append(6)  # Adding an element to the end of the list
print(my_list)
my_list.remove(3)  # Removing an element from the list
print(my_list)
my_list.insert(2, 10)  # Inserting an element at a specific index
print(my_list)
my_list[0] = 44
print(my_list)
print(my_list[1:4])  # Slicing the list
print(10 in my_list)  # Checking if an element is in the list
print(my_list.count(10))  # Counting occurrences of an element
my_list.pop(3)
print(my_list)


zoo = ["lion", "tiger", "bear", "elephant"]
zoo.append("giraffe")
print(zoo)
print(zoo[0:3])
print("tiger" in zoo)
print(zoo.pop(3)) 
zoo.pop(0) 
print(zoo)