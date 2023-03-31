'''
first class functions, using functions as parameter
in js it's called callback 
'''
def divide(divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return divided / divisor


def calculate(*values, operator):
    return operator(*values)

result = calculate(20,0, operator=divide)
print(result)