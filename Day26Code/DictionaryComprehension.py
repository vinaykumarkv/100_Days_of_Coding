# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleana', 'Florine']
#
# student_scores = {student:random.randint(1,100) for student in names}
#
# print(student_scores)
#
# passed_students = {student: value for (student, value) in student_scores.items() if value > 35}
#
# print(passed_students)


#
# list_of_strings = input().split(' ')
# print(list_of_strings)
#
# result = {key: len(key) for key in list_of_strings}
# print(result)

weather_report = {
    'Monday': 12,
    'Tuesday': 24,
    'Wednesday': 15,
    'Thursday': 20,
    'Friday': 21,
    'Saturday': 18,
    'Sunday': 17
}

result = {key: round((value * (9 / 5)) + 32) for (key, value) in weather_report.items()}
print(result)