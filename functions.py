
# function

def add(a, b):
    return a + b

print(add(5, 3))  # Calling the function with arguments


def mergeNames(first_name, last_name, age):
    full_name = first_name + " " + last_name
    return {
        'first_name' : first_name,
        'last_name': last_name,
        'age': age,
    }


print(mergeNames("John", "Doe", 30))