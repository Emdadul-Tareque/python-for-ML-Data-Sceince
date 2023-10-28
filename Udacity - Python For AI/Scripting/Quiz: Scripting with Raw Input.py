names =  input("Enter names separated by commas: ").split(',')
assignments =  input("Enter Assignment Counts separated commas: ").split(',')
grades = input("Enter Grades Separated by Commas: ").split(',') 

print(names)

for name, assignment, grade in zip(names, assignments, grades):
    potential_grade = int(grade) + 2 * int(assignment)
    message = f"Hi {name},\n\nThis is a reminder that you have {assignment} assignments left to \
submit before you can graduate. You're current grade is {grade} and can increase \
to {potential_grade} if you submit all assignments before the due date.\n\n"
    
    print(message)


