hej = (9, 2, 4, 5)
print(hej)

hej = [1,2,3]
print([num + 1 for num in hej])

hej = ["1","2","3"]
print([int(num) for num in hej])


def get_second_character(item):
    print(item[1])
    return item[1]


test = ["bim", "ben"]
test.sort(key=get_second_character)
print(test)

test.append("asd")
print(test)

y = (1,2,3)

names = ("bejamin", 2, "hello")
print(names[1])
a = tuple("asd")
print(a[0])
names = ("bejaminasd", 3)
print(names)

names = ["asd", "a"]
print(names)

names[0] = 12
print(names)

h = names.pop(-1)
print(names)
names.extend([2,3,4])
print(names)

names = [1,2,3,4]
for number in names:
    print(number)

names = [number * 2 for number in names]
print(names)


def get_name_length(name):
    return len(name)


names = ["asd", "asddf", "b"]
names.sort(key = get_name_length, reverse=True)
print(names)

print("b" in names)

o = {
    "name": "benjamin",
    "age": 23

}
print(o)
print(o['name'])
print(o['age'])
del o["age"]
print(o)
o["name"] = "peter"
print(o)
n = {
    "student": o
}

print(n)


def is_logged_in(number):
    return number[-1] == "a"

if is_logged_in("hejsa"):
    print("logged in")
elif is_logged_in("hejsa"):
    print("not logged in")
else:
    print("in else")

