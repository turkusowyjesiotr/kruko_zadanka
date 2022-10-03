# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key=lambda student: student[1])  # sorting students by grade
    # list comprehension that returns list without all students with lowest grade
    students = [student for student in students[1:] if student[1] != students[0][1]]
    # list comprehension that returns list with all second worst grade students
    results = [student for student in students if student[1] == students[0][1]]
    # sorting students alphabetically by name and printing results
    for result in sorted(results, key=lambda student: student[0]):
        print(result[0])
