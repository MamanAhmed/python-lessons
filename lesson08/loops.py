value = 1
# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))


names = ["Luffy", "Zoro", "Nami", "Usopp",
         "Sanji", "Chopper", "Robin", "Franky", "Brook"]

for name in names:
    print(name)

for char in "Mississippi":
    print(char)

for name in names:
    if name == "Usopp":
        break
    print(name)

print("")

# for name in names:
#     if name == "Usopp":
#         continue
#     print(name)

# for x in range(4):
#     print(x)

# print("")

# for x in range(2, 4):
#     print(x)

for x in range(0, 101, 5):
    print(x)
else:
    print("Glad that\'s over")


names = ["Luffy", "Zoro", "Nami", "Usopp",
         "Sanji", "Chopper", "Robin", "Franky", "Brook"]

actions = ["eats", "sleeps", "navigates", "runs",
           "cooks", "heals", "reads", "builds", "sings"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")


# for action in actions:
#     for name in names:
#         print(name + " " + action + ".")


for name, action in zip(names, actions):
    print(name + " " + action + ".")
