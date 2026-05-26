country = "India"
state = "Maharashtra"

import calculate_grade as cg
import random
import math



homework_assignement_grades = {
    "Maths": 85,
    "Science": 90,
    "English": 80,
}

# def calculate_average_grade(grades):
#     total = sum(grades.values())
#     count = len(grades)
#     average = round(total / count)
#     return average


average_grade = cg.calculate_average_grade(homework_assignement_grades)
print(f"The average grade for the homework assignments is: {average_grade}")

type_of_grades = ["A", "B", "C", "D", "E", "F"]
random_grade = random.choice(type_of_grades)
print(f"The random grade selected is: {random_grade}")

print(f"The value of pi is approximately: {math.pi}")
print(f"The value of pi is approximately: {math.sqrt(434343434343434343676)}")