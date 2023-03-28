from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")



friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

# instead of this use lambda
def get_friend_name(friend):
    return friend["name"]


# print(search(friends, "Rolf Smith", get_friend_name))

# print(search(friends, "Rolf Smith", lambda friend: friend["name"]))

print(search(friends, "Anne Pun", itemgetter("name")))