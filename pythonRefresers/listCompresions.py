# numbers = [1,3,4]
# doubled = [x * 2 for x in numbers]

# for num in numbers:
#     doubled.append(num * 2)


# friends = ["Sam","Rolf", "Samantha", "Saurabh","Jen"]

# starts_s = [ friend for friend in friends if friend.startswith("S")]

# # for friend in friends:
# #     if friend.startswith("S"):
# #         starts_s.append(friend)

# print(friends[0] is starts_s[0])
# print("friends: ", id(friends), "starts_s:", id(starts_s))

# Assignment from udemy

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    "name": 'Jose',
    "school":"Computing",
    "grades": (66, 77, 88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
# def average_grade(data):
#     grades =  data['grades'] # Change this!
#     print(grades)
#     # return sum(grades) / len(grades)

# average_grade(student)
# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
# def average_grade_all_students(student_list):
#     total = 0
#     count = 0
#     for student in student_list:
#         total = total + sum(student['grades'])
#         count = count + len(student['grades'])
#         # Implement here
#         return total / count
    
def mutiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

mutiply(1,2,4)


# def add(x,y):
#     return x+y

# nums = [3,4]
# # print(add(*nums))

# nums ={"x": 15, "y": 34}

# print(add(**nums))

def apply(*args, operator):
    if operator == "*":
        return mutiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1,3,6,7, operator="*"))


