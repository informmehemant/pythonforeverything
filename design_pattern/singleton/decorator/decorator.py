user = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return "1234"

def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"
    
# def secure_function(func):
#     if user["access_level"] == "admin":
#         return func

# calling functions within functions

def make_secure(func):
        def secure_function():
             if user["access_level"] == "admin":
                  return func()
             else:
                  return f"No admin permission for {user['username']}"
        return secure_function

get_admin_password = make_secure(get_admin_password)

# print(secure_get_admin())
print(get_admin_password())