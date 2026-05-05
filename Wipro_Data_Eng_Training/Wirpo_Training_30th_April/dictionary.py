#Dictionary
student = {
    "name" : "Rahul",
    "age"  : 22,
    "course" : "python"
}
print(student)

print(student["name"])
print(student["course"])

#adding new key value pair
student["city"] = "Hyderabad"
print(student)

#update the data
student["age"] = 25
print(student)

del student["city"]
print(student)

#Key Interaction
for key in student.values():
    print(key)

#value interaction
for value in student.values():
    print(value)

#loop through key-value pairs
for key, value in student.items():
    print(key, value)


