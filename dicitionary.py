# dictionary.py

usre_disctionary = {
    "name": "Alice",
    "age": 28,
    "city": "New York"
}

print(usre_disctionary["name"])  # Output: Alice
print(usre_disctionary.get("city"))  # Output: New York

usre_disctionary["salary"] = 4100000  # Adding a new key-value pair

print(usre_disctionary)

print(len(usre_disctionary))  # Output: 4

print("age" in usre_disctionary)  # Output: True

print(usre_disctionary.pop("age"))  # Output: 28
print(usre_disctionary)

# usre_disctionary.clear()  # Removing all key-value pairs
# print(usre_disctionary)  # Output: {}

for key in usre_disctionary:
    print(key)

for key, value in usre_disctionary.items():
    print(f"{key}: {value}")

# usre_disctionary2 = usre_disctionary
# usre_disctionary2.pop("name")

# print(usre_disctionary)  # Output: {'city': 'New York', 'salary': 4100000}
# print(usre_disctionary2)  # Output: {'city': 'New York',

usre_disctionary2 = usre_disctionary.copy()  # Creating a copy of the dictionary
usre_disctionary2.pop("name")

print(usre_disctionary)  
print(usre_disctionary2)

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}


for key, value in my_vehicle.items():
    print(f"{key}: {value}")


vechile2 = my_vehicle.copy()
vechile2["number_of_tires"] = 4
vechile2.pop("mileage")

print(my_vehicle)
print(vechile2)