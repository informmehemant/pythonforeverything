#  * args means its collecting
# (1, 2, 4)
# def multiply(*args):
#     total = 1
#     for arg in args:
#         total *= arg
#     return total


# multiply(1,2,4)

# def add(x,y):
#     return x + y

# nums = [3,5]
# # add(*nums)

# numsDict = {'x': 2, 'y': 3}
# # first methods is this way 
# print(add(x=numsDict['x'], y=numsDict['y']))

# # second method is to uses **

# print(add(**numsDict))

# def apply(*args, operator):
#     if operator == "*":
#         return multiply(*args)
#     elif operator == "+":
#         return sum(args)
#     else:
#         return "No valid operator to apply()"
    

# print(apply(1,2,2, operator="*"))

# this is one way
def named(**kwargs):
    print(kwargs)


named(**{"name":"Bob", "ages": 34})


# def named2(name, age):
#     print(name, age)

# details ={"name": "Bob", "age": 25}

# named2(**details)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,2,3, **{"name": "Bob", "age": 45})


