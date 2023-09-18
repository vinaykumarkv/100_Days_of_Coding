student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}
for key in student_scores:
    print (key)
    print(student_scores[key])
student_grades ={}
print(student_scores)
for key in student_scores:
    if 101 > student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif 91 > student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif 81 > student_scores[key] > 71:
        student_grades[key] = "Acceptable"
    elif 81 > student_scores[key] > 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
 
for key in student_grades:
    print (key)
    print(student_grades[key])
print(student_grades)   

