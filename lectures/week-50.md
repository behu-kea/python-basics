

# Week 50 - Debugging, conditional logic and control flow

Join [here](https://teams.microsoft.com/l/meetup-join/19:rkh5Vl9ssYsl6go6ZjONTrjgaxsha3T0RyQPdiU2I8E1@thread.tacv2/1639408908489?context=%7B%22Tid%22:%22d10c3c6e-c228-4944-8b6a-6067c6afe3c9%22,%22Oid%22:%2232e4ca2f-6ba3-4bdf-bb5f-7414a5ae6d0b%22%7D)



## Overview

- Feedback on methods project
  - **Rigtig** gode variabelnavne, men husk `ask_show_titel` ikke `askshowtitel`
  - God brug af funktioner, argumenter, parametere og return, **men** brug funktioner meget mere!
  - Try and wrap all code in functions now
  - Fedt med `get_full_name`
  - 
- Peer instruction
- Undervisning
- Opgaver



## Peer instruction



### Question 1

```python
def add(a, b):
	sum = a + b
	print(sum)
	
numbers_sum = add(1, 2)
print(numbers_sum)
```

What is printed when `numbers_sum` is printed?

- `3`
- `None`
- `12`
- `1, 2`
- Error thrown



### Question 2

```python
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
```

What will be printed when `print_message` gets printed?

- `"That's a lot of money"`
- `"That's an ok amount of money"`
- `"That's not a lot of money"`
- `None`
- Error thrown





- Logical operators
  - Boolean
  - `==`
  - `!=`
  - `<`, `>`, `<=`, `>=`
  - `and`
  - `or`
  - `not`
  - password
    - contains word `hej`
    - does not contain word `password`
    - Longer than 5 characters
  
- If, else if, else

  - Balance example

- Loop control: `break`, `continue`

  - Break when i == 2. stopping at 2
  - continue when i == 2, skipping 2

- `try`, `except`

  - ```
    try:
        a = 1/0
    except Exception as e:
        print(e)
    ```

- `random`

- Debugging



## Exercises

- 8.1.1
- 8.2.1
- 8.3.2
- 8.5.1
- 8.6.1



## Level 2



### Exercise 1

Create a game where two users put in their names. Now two dice are rolled, the user with the highest number wins



### Exercise 1.1

Write a function that checks if a cpr number is valid



### Exercise 2

8.8



## Project for next class

[Rock paper scissor 🤘🔖✂](../projects/rock-paper-scissor.md) 



## Christmas challenges 🎄🎅❄️☃️

These christmas challenges are completely optional. They are also a bit more advanced so to solve some of them you would need to know about lists. You can read up on lists in chapter 9.2. This is anyways required reading for week 1. 



Advent of code is a coding challenge that has run for many years. Each day there is a new challenge. You need to sign up if you want to really participate. You could also just solve the problem being formulated. 

- https://adventofcode.com/2021/day/1
- https://adventofcode.com/2021/day/2
- https://adventofcode.com/2021/day/3



## Before next class

Check if you are ready with this quiz: https://realpython.com/quizzes/pybasics-conditional-logic/





```
elif balance <= 5000 and balance > 1000:
    print("That's an ok amount of money")
else:
    print("That's not a lot of money")
```
