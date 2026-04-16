
"""

# Printing a list of courses

courses = ["DataScience", "DataAnalytics", "Python", "JavaScript"]

for course in courses:
    print(course)

# Iterating through a List

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)

# Generating a Number Sequence
for i in range(1, 6):
    print("Number:", i)

# Counting and displaying course names

courses = ["DataScience", "DataAnalytics", "Python", "JavaScript"]
count = 1

for course in courses:
    print(f"Course {count}: {course}")
    count += 1

# Finding and printing the length of each course name

courses = ["DataScience", "DataAnalytics", "Python", "JavaScript"]

for course in courses:
    length = len(course)
    print(f"The course name '{course}' has {length} characters.")

"""## 2. Nested 'for' loop"""

# Multiplication table

for i in range(1, 6):
    for j in range(1, 11):
        product = i * j
        print(f"{i} * {j} = {product}")
    print()

# Printing a Pattern
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Creating a Matrix

rows = 3
cols = 3
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j)
    matrix.append(row)

for row in matrix:
    print(row)

# Matrix multiplication

matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(matrix_A)):
    for j in range(len(matrix_B[0])):
        for k in range(len(matrix_B)):
            result[i][j] += matrix_A[i][k] * matrix_B[k][j]

for row in result:
    print(row)

"""## 'while' loop"""

#Printing course names until a condition is met

courses = ["DataScience", "DataAnalytics", "Python", "JavaScript"]
index = 0

while index < len(courses):
    print(courses[index])
    index += 1

#Counting the number of characters in course names

courses = ["DataScience", "DataAnalytics", "Python", "JavaScript"]
index = 0

while index < len(courses):
    course = courses[index]
    length = len(course)
    print(f"The course '{course}' has {length} characters.")
    index += 1

# Counting Down

count = 5

while count > 0:
    print(count)
    count -= 1

# Right Triangle

row = 1
while row <= 4:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row += 1

# Square
side = 1
while side <= 3:
    width = 1
    while width <= 3:
        print("*", end=" ")
        width += 1
    print()
    side += 1

