users = ["Dave", "Tom", "Jane"]

data = ["Dave", 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index("Jane"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])


print(len(data))

print(users)
users.append("Maman")
print(users)

users += ["Jason"]
print(users)

users.extend(["Tony", "Christopher"])
print(users)


users.insert(0, "Furio")
print(users)

# Inserting at a specific index
users[2:2] = ["Carmela", "Meadow"]
print(users)

# Replacing elements
users[1:3] = ["Paulie", "Silvio"]
print(users)

users.remove("Tom")
users.remove("Jane")
users.remove("Jason")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

data.clear()
print(data)

users[1:2] = ["luffy"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [42, 6, 2, 50, 32,]

nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

# Creating copys
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))


# Tuples
mytuple = tuple(("Luffy", 25, True))

anothertuple = ("Zoro", 28, False)

print(mytuple)
print(type(mytuple))

print(anothertuple)
print(type(anothertuple))

newlist = list(mytuple)
print(newlist)

newlist.append("Pirate King")

newtuple = tuple(newlist)
print(newtuple)

print(type(newtuple))

(name, age, *ispirate) = newtuple

print(name)
print(age)
print(ispirate)
