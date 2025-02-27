# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Accessing items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key/value pairs as tuples
print(band.items())

# Check if key exists
print("guitar" in band)
print("triangle" in band)

# Changle values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # returns a tuple
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()

del band2

# Copy dictionaries

# band2 = band  # creates a reference

# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()

band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
band3["drums"] = "Jason"
print("Good copy!")
print(band)
print(band3)

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals",
}

member2 = {
    "name": "Page",
    "instrument": "guitar",
}

band = {
    "member1": member1,
    "member2": member2,
}

print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed

nums = {1, 2, 2, 3}

print(nums)

# True is dupe of 1, False is a dupe of zero

nums = {1, True, 2, False, 3, 4, 0}

print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in a set by index or key
# print(nums[0])  # TypeError: 'set' object is not subscriptable

# add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}

nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictionaries too.


# Merge to sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates

one = {1, 2, 3}
two = {2, 3, 4}

mynewset = one.intersection(two)
print(mynewset)


# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
