
myList = [1, 2, 3, 43, 5]

# for number, index in enumerate(myList):
#     print(f"Index: {index}, Number: {number}")


strData = "Hello, World!"

# for char in strData:
#     print(char)


# while True:
#     user_input = input("Enter a number (or 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         print("Exiting the loop. Goodbye!")
#         break
#     try:
#         number = float(user_input)
#         print(f"You entered: {number}")
#     except ValueError:
#         print("Invalid input. Please enter a valid number or 'exit'.")


my_list_d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# for day in my_list_d:
#     if day == "Monday":
#         continue  # Skip the rest of the loop for Monday
#     print(f"Today is {day}.")
#     print(f"Today is {day}.")
#     print(f"Today is {day}.")

x = 0

while x < 3:
    x = x + 1
    for i in my_list_d:
        if i == "Monday":
            print("Skipping Monday......................")
            continue  # Skip the rest of the loop for Monday
        print(f"Today is {i}.")
