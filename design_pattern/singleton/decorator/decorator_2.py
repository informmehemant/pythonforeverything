user = {"username": "jose", "access_level": "admin"}


def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"
    

def make_secure(func):
        # internal function name can be used seperately, 
        # calling print(get_admin_password.__name__)
        def secure_function():
             if user["access_level"] == "admin":
                  return func()
             else:
                  return f"No admin permission for {user['username']}"
        return secure_function

@make_secure
def get_admin_password():
    return "1234"


# get_admin_password = make_secure(get_admin_password)
# print(secure_get_admin())

print(get_admin_password.__name__)

print(get_admin_password.__name__)