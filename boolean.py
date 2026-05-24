
like_coffees = True
like_tea = False

if like_coffees:
    print("I like coffee!")
if like_tea:
    print("I like tea!")


favorite_drink = "coffee"

print(type(like_coffees))  # Output: <class 'bool'>
print(type(like_tea))  # Output: <class 'bool'>
print(type(favorite_drink))  # Output: <class 'str'>


# comparison operators
print( 1 == 1)
print(1 != 1) 
print(1 > 0)
print(1 < 2)
print(1 >= 1)
print(1 <= 2)

# logical operators
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False
# combining comparison and logical operators
age = 25
is_adult = age >= 18
has_id = True
can_enter_club = is_adult and has_id
print(can_enter_club)  # Output: True

x = 15
if x > 0 and x < 10:
    print("x is a positive single-digit number.")
elif x >= 10:
    print("x is a positive number with two or more digits.")
else:
    print("x is not a positive single-digit number.")

print((5 > 3) and (2 < 4))  # Output: True
print((5 > 3) or (2 > 4))   # Output: True


mark = 58

if mark >= 90:
    print("Grade: A")
elif mark >= 80:
    print("Grade: B")
elif mark >= 70:
    print("Grade: C")
elif mark >= 60:
    print("Grade: D")
else:
    print("Grade: F")