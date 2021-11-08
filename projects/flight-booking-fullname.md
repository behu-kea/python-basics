# Flight booking fullname function



 A customer from a flight booking website has asked  for our help creating a specific part of their application:

When a user books a flight they **write their firstname and surname**, but when the ticket is printed a **fullname should be displayed**. It is our responsibility to create that.

Create a function called `getFullname` that returns a fullname. It should have two parameters: `firstname` and `surname`.

```python
fullname = getFullname("Benjamin", "Hughes")
print(fullname) # "Benjamin Hughes"
```

 `firstname` and `surname` should come from the user



## Formal fullname

On the flight website the user has the possibility to **check a checkbox** that **indicates** if the user wants to be **adressed formally**. They also specify their gender. Lets also change `getFullname` to include support for formal name.

Create two extra parameters one that will contain the gender, the other that will indicate if the user wants to be adressed formally or not. 

```python
getFullname("Camilla", "Jensen", "female", True) # returns "Lady Camilla Jensen"
getFullname("Benjamin", "Hughes", "male", False) # returns "Benjamin Hughes"
```

Now create a small program simulating a bit of a flight booking process using the method you just created and `input`. 

*Inspired from https://github.com/HackYourFuture-CPH/JavaScript/blob/master/javascript1/week2/homework.md*

