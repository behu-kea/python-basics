# BMI
# Create a new python file that asks the user for their weight and height.
# Using the weight and height calculate the BMI and print that to the user in a user friendly way

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height / 100) ** 2

print(f"You BMI is {BMI}")

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")


