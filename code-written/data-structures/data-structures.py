
def get_winner(player_move_1, player_move_2):
    # kode logik
    return 0


#move_1 = input("player 1 what is your move?")
#move_2 = input("player 2 what is your move?")
#result = get_winner(move_1, move_2)
#print(result)

# Tuples
grades = (7, 5, 10, 12, 12, 12)
print(grades)
print(grades[0])
print(grades[1:5])
print(len(grades))

asd_string = "asd"
weird_tuple = (asd_string, True, 12, 3.4)
print(weird_tuple[0])

# List (array in other languages)
names = ["Peter", "johanne", "Mie"]
print(names)
print(names[0])
print(names[1:5])
print(len(names))
names[0] = "Hans"
print(names)
# Tilføj et enkelt element i slutningen af listen
names.append("Tommy")
print(names)
# fjern et enkelt element ved et bestemt index
names.pop(0)
print(names)

surnames = ["Hansen", "Jensen"]
# Tilføjer vi en anden liste i slutningen af listen
names.extend(surnames)
print(names)
# se hvordan man kan bruge metoder på en bestemt datatype
#print(help(names))

#
#for i in range(3):
    #print(i)


for name in names:
    print(name)

numbers = [1, 2, 3, 4]
print(numbers)
# 2, 4, 6, 8
# Mappe
number_doubled = [x * 2 for x in numbers]
print(number_doubled)

prices = [100, 1000, 10]
prices.sort(reverse = True)
print(prices)

print(400 in prices)
print(100 in prices)


# Dictionary
# key, value store
hans_student = {
    "name": "Hans",
    "age": 23,
    "grades": [5, 7, 12, 12]
}

yvonne_student = {
    "name": "Yvonne",
    "age": 27,
    "grades": [5]
}

print(hans_student)
print(hans_student["name"])
print(hans_student["age"])
print(hans_student["grades"])
hans_student["name"] = "Per"
print(hans_student["name"])
print(hans_student)
del hans_student["name"]
# print(hans_student)
# excel, database

students = [hans_student, yvonne_student]
for student in students:
    print(student)


municipality_inhabitants = {
    "helsingør": 23300,
    "københavn": 12998,
}
print(municipality_inhabitants["københavn"])
municipality_inhabitants["helsingør"] = 1234
print(municipality_inhabitants)

