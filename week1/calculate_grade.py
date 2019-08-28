exams = 50
home_assignments = 39
total_points = exams + home_assignments # the total points is the sum of the exams score and home assignment


if total_points >= 90:
    final_grade = 'A'
elif total_points > 80 and total_points < 90:
    final_grade = 'B'
else:
    final_grade = 'C'

print(final_grade)