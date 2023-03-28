# friends_ages = [
#     {"name":"Rolf", "age": 24},
#     {"name":"Adam", "age": 44},
#     {"name":"Anne", "age": 94}
# ]

# friends_ages["Rolf"] = 20

# print(friends_ages["Adam"])

student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100
}

# for student in student_attendance:
#     print(f"{student}:{student_attendance[student]}")

for student , grade in student_attendance.items():
    print(f"{student}:{grade}")

# x, y = 5, 11

# t = 5,6
# x,y = t


print(list(student_attendance.items()))
people = [("Bob", 43, "Mechanic"), ("James", 23, "Artist"), ("Harry", 43, "Lecturer")]

# destructuring code ....

for name, age, profression in people:
    print(f"Name: {name}, Age: {age}, Profession: {profression}")

person = ("Bob", 43, "Mechanic")
name, _, profession = person

head, *tail = [1,2,3,4,5]
print(head)
print(tail)