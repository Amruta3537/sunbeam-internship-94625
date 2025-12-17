# list of dictionaries


students = [
        {'rollno':1, 'name':"abc"},
        {'rollno':2, 'name':"xyz"},
        {'rollno':3, 'name':"pqr"}
    ]


print(students)

students.append({'rollno':4, 'name':"def"})

print(students)

students.pop()
print(students)

students.remove({'rollno':3, 'name':"pqr"})

# for value in students:
#     print(f"rollno- {value["rollno"]}, Name- {value["name"]}")