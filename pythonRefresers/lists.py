l = ["bob","Rolf","Anne"]

# can't add and remove from tuple
t = ("Bob","Rold","Anne")

# sets
s = {"BOB","Rolf","Anne"}


friends = {"Bob","Rolf","Anne"}
abroad ={"Bob","Anne"}

local_friend = friends.difference(abroad)
total_friend = friends.union(abroad)
total_friend = friends.intersection(abroad)
print(local_friend)

print(total_friend)