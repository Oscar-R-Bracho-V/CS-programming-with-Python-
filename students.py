student_heights = input("Input a list of student heights: ").split()
print(student_heights)

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

total_height = 0
total_students = 0
for height in student_heights:
    total_height += height
    total_students += 1

average_height = round(total_height / total_students)

print(f"Total height: {total_height}")
print(f"Total students: {total_students}")
print(f"Average height: {average_height}")
