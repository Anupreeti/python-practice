student = {"name":"Preeti",
           "roll_no":"12",
           "GPA":"456"}
print(student)
student["GPA"] = 500
student["email"] = "pree@gmail.com"
print(student)
print(student["name"])
for name,item in student.items():
    print(item)
