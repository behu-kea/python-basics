# Methods project



## Flight booking fullname function

A customer from a flight booking website has asked  for our help creating a specific part of their application:

When a user books a flight they **write their firstname and surname**, but when the ticket is printed a **fullname should be displayed**. It is our responsibility to create that.

Create a function called `getFullname` that returns a fullname. It should have two parameters: `firstname` and `surname`.

```python
fullname = getFullname("Benjamin", "Hughes")
print(fullname) # "Benjamin Hughes"
```

 `firstname` and `surname` should come from the user



### Formal fullname

On the flight website the user has the possibility to **check a checkbox** that **indicates** if the user wants to be **adressed formally**. They also specify their gender. Lets also change `getFullname` to include support for formal name.

Create two extra parameters one that will contain the gender, the other that will indicate if the user wants to be adressed formally or not. 

```python
getFullname("Camilla", "Jensen", "female", True) # returns "Lady Camilla Jensen"
getFullname("Benjamin", "Hughes", "male", False) # returns "Benjamin Hughes"
```



### Using `getFullname`

Now simulate a bit of a flight booking process using the method you just created and `input`. 

Try and create a userfriendly application that asks for the users details and then shows the correct fullname



## Questions

- What is the scope of a variable (in function)?
- What is the difference between local and global variable?
- What is the difference between a parameter and an argument?



## Trip calculator - optional

Let's use functions to calculate your trip's costs:

- Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. So, the function `hotel_cost` should return 140 * nights.

- Define a function called `plane_ride_cost` that takes a string `city`, as argument. The function should return a different price depending on the location, similar to the code example above. Below are the valid destinations and their corresponding round-trip prices.

  Charlotte - 183
  Tampa - 220
  Pittsburgh - 222
  Los Angeles - 475



Below your existing code, define a function called `rental_car_cost` with an argument called `days`. Calculate the cost of renting the car: Every day you rent the car costs $40. 

If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total. You cannot get both of the above discounts.

Then, define a function called `trip_cost` that takes two arguments, `city` and `days`. Like the example above, have your function return the sum of calling the `rental_car_cost(days)`, `hotel_cost(days)`, and `plane_ride_cost(city)` functions.

Now modify your `trip_cost` function definition. Add a third argument, `spending_money`. Modify what the `trip_cost` function does. Add the variable `spending_money` to the sum that it returns



*Inspired from https://github.com/HackYourFuture-CPH/JavaScript/blob/master/javascript1/week2/homework.md*



## Handin

Handin your project here: https://kea-fronter.itslearning.com/LearningToolElement/ViewLearningToolElement.aspx?LearningToolElementId=951856



**Deadline: Sunday 12/12 23:59**



### How to handin

- Navigate to the link above
- Click `Besvar opgave`
- Leave `Dit svar` blank
- Add your `.py` file where it says `Tilføj filer`
  - You can do that by dragging and dropping 
  - Or click the area and select the `.py` file 
- Click `Send`
