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

