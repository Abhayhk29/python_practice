def calculate_average_grade(grades):
    total = sum(grades.values())
    count = len(grades)
    average = round(total / count)
    return average


