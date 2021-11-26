'''
Let a user input his/her password. Now we have to figure out if the password is valid. There are the rules:
Must be longer than 8 characters
Cannot contain the word password
Has to have a special character
Must not start with a number
'''

password = input("Please put in your password to check validity 👉")
password_lower = password.lower()
isPasswordLongEnough = len(password_lower) > 8
containsWordPassword = 'password' in password_lower
startsWithNumber = password_lower[0].isdecimal()
# Taken from here https://stackoverflow.com/a/57062899
containsSpecialCharacter = any(not c.isalnum() for c in password_lower)

isPasswordValid = isPasswordLongEnough and not containsWordPassword and not startsWithNumber and containsSpecialCharacter
if isPasswordValid:
    print("Password valid")
else:
    print("Password invalid")

# Simple scoring algorithm
score = 0
if containsSpecialCharacter:
    score = len(password_lower) * 2
else:
    score = len(password_lower)


# This will print good if a password is long but not valid. Could be fixed!
password_score_text = ""
if score < 10:
    password_score_text = 'bad'
else:
    password_score_text = 'good'

print(f'Here is your score: {score}. That makes your password {password_score_text}')


