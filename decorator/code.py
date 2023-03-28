import functools
user = {"username": "jose", "access_level": "user"}


# decorator functions are functions which are func within functions
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_functions(*args, **kwargs):    
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."
        return secure_functions
    return decorator


# # internally this is hapenning for make_secure password

# get_admin_password = make_secure(get_admin_password)

@make_secure("admin")
def get_admin_password():
    return "admin:1234"

@make_secure("user")
def get_billing_password():
    return "user:1234"



print(get_admin_password())