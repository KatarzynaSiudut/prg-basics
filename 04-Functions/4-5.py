###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''

    if points > 10:
        grade = 'Fail'
    if points >= 10:
        grade = 'Satisfactory'
    if points >= 14:
        grade = 'Good'
    if points >= 18:
        grade = 'Excellent'
    return grade

test_result = 10
final_grade = pts_to_grade(test_result)
print('You scored 10 points on the test. Your final grade is: ', final_grade)