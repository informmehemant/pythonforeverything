users = [
    (0, "Bop","password"),
    (1, "Rolf","bob123"),
    (2, "Jose","longp4assword"),
    (3, "username","1234"),
]
# dictionay compressions
username_mapping = { user[1]: user for user in users}
print(username_mapping)

user_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_,username, password = username_mapping[user_input]

if password_input == password:
    print("your details are correct!")
else:
    print("password is incorrect!")




