
# add_one function without recursion
def add_one_loop(num):

    for i in range(10):
        num += 1
        print(num)
    return num


print(add_one_loop(0))


# add_one function with recursion


def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)
