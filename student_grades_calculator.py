def calculate_grade(avg):
    if avg >= 80:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 40:
        return 'C'
    else:
        return 'Fail'

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i+1}")
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks in 3 subjects separated by space: ").split()))
    total = sum(marks)
    avg = total / 3
    grade = calculate_grade(avg)
    students.append({'name': name, 'total': total, 'avg': avg, 'grade': grade})
    print(f"Result: {name} - Total: {total}, Avg: {avg:.2f}, Grade: {grade}")

topper = max(students, key=lambda x: x['avg'])
print(f"\n Class Topper: {topper['name']} with Average {topper['avg']:.2f}")