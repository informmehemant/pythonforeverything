'''
Real time usage of factory pattern  in user and role creations
'''
# abstract User class


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class AdminUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = 'admin'


class RegularUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = 'regular'


class Guest(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = 'guest'

# User Factory


class UserFactory:
    @staticmethod
    def create_user(user_type, name, email):
        if user_type == 'admin':
            return AdminUser(name, email)
        elif user_type == 'regular':
            return RegularUser(name, email)
        else:
            return Guest(name, email)


# initializing user factory

admin = UserFactory.create_user('admin', 'hemant', 'info90.hemant@gmail.com')

guest = UserFactory.create_user('guest', 'manu', 'manu@gmail.com')

print(admin)

print(guest)
