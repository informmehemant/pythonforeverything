# def add(x,y):
#     return x + y

# add = (lambda x,y: x*y)(3,4)
# print(add(7,6))

# def double(x):
#     return x * 2

sequence = [1,4,5,6,9]

# doubled = [x * 2  for x in sequence]
# or

# double = [double(x) for x in sequence]
# or

# double mapped in sequences

# double = map(double, sequence)

#  also can be use as lambda functions
# map will return map of objects so convert it into list
double = list(map(lambda x: x * 2, sequence))
# 

print(double)