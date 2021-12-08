import math
# 6.2.1


def cube(number):
    # print(number)
    # print(math.pow(number, 3))
    return math.pow(number, 3)


# print(cube(4))
four_cubed = cube(4)
print(four_cubed)


def add(a, b):
    sum = a + b
    print(sum)


numbers_sum = add(1, 2)
print(numbers_sum)

#cube(6)


def get_balance_message(balance):
  print_message = ""
  if balance > 5000:
    print_message = "That's a lot of money"
  elif balance <= 5000 and balance > 1000:
    print_message =  "That's an ok amount of money"
  else:
    print_message =  "That's not a lot of money"

get_balance_message(5000)
print(print_message)
