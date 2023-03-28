from operator import itemgetter
def search(sequence: list, expected: str,finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Rian", "age": 54},
    {"name": "Ganam Style", "age": 44},
]

def get_friend_name(friend):
    return friend['name']

# instead of using get_friend_name we can use lambda friend : friend["name"]
# there ways we can use it 
# #calling first order functions
# print(search(friends, "Ganam Style", get_friend_name))
# # # calling through lambda
# print(search(friends, "Ganam Style", lambda friend : friend["name"]))
# #through itemgetter uses internally uses lambda
print(search(friends, "Ganam Style", itemgetter("name")))