import random

hej = 2
def print_conditional():
    if True:
        print("asdds")
    else:
        print("in else")


print_conditional()


def get_balance_message(balance):
    print_message = ""
    if balance > 5000:
        print_message = "That's a lot of money"
    elif balance <= 5000 and balance > 1000:
        print_message =  "That's an ok amount of money"
    else:
        print_message =  "That's not a lot of money"
    return print_message


print_message = get_balance_message(5000)
print(print_message)

number = 1
print(number == 1)
print(1 > 3)
print(100 >= 3)
print(3 >= 3)
print("and")
print(1 == 1 and 2 == 2)
print(1 == 2 and 2 == 2)
print("or")
print(1 == 1 or 2 == 2)
print(1 == 2 or 2 == 2)
print(1 == 2 or 2 == 4)
print("not")
print(not 1 == 1)


print("password checker")
# contains word hej
# does not contain word password
# Longer than 5 characters
def check_password(password):
    is_password_long_enough = len(password) <= 5
    is_hej_in_password = "hej" in password
    does_not_contain_password = "password" not in password
    is_password_valid = is_password_long_enough and is_hej_in_password and does_not_contain_password
    if is_password_valid:
        return True
    else:
        return False



check_password("benjaminhej123")


## if, else if, else
print("if, else if, else -------------")
balance = 1000
if balance > 5000:
    print("That's a lot of money")
elif balance <= 5000 and balance > 1000:
    print("That's an ok amount of money")
else:
    print("That's not a lot of money")

print("fortsætter")

for i in range(0, 4):
    if i == 2:
        break
    print(i)
print("fortsæt")

for i in range(0, 4):
    if i == 2:
        continue
    print(i)
print("fortsæt")


try:
    number_string = input("Input a number")
    number = int(number_string)
except Exception as e:
    print(e)
    print("Please input a valid number")


## randomness
print(random.randint(10, 20))
