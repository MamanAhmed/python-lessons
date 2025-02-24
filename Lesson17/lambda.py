from functools import reduce
def squared(num): return num * num
# lambda num : num * num


print(squared(2))


def addTwo(num): return num + 2
# lambda num: num + 2


print(addTwo(12))


def sum_total(a, b): return a + b
# lambda a, b: a + b


print(sum_total(10, 8))


#####################################

def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


####################################


numbers = [3, 7, 12, 18, 20, 21]


# map applies function to every element
squared_nums = map(lambda num: num * num, numbers)  # Creates a map object

print(list(squared_nums))


####################################


# Filter applies function and only returns elements that evaluate to True


odd_nums = filter(lambda num: num % 2 != 0, numbers)  # Creates a filter object

print(list(odd_nums))


lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)


lambda acc, curr: acc + len(curr)

names = ["Dave Gray", "Sara Ito", "John Jacob Jingleheimerschimdt"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0
                    )

print(char_count)
