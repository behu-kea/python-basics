# Week 49 - Functions and loop



## Preparation videos

- [https://youtu.be/8fN8h7REnyo](https://youtu.be/8fN8h7REnyo)
- [https://youtu.be/YZ11aS9QV6c](https://youtu.be/YZ11aS9QV6c)
- [https://youtu.be/J8hP1MTbBeg](https://youtu.be/J8hP1MTbBeg)
- [https://youtu.be/GDEaklG5Gbw](https://youtu.be/GDEaklG5Gbw)



<!--

## Peer instruction



### Question 1

```python
name = "benjamin"
size_of_name = len(name)
last_character = name[size_of_name]
print(last_character)
```

What will this program print?

1. `i`
2. `n`
3. `8`
4. `benjamin`
5. Error thrown



### Question 2

```python
print("KøBeNhAvN".lower()[3:6])
```

What will this program print?

1. `eNhA`
2. `enha`
3. `enh`
4. `københavn`
5. `kebabenhavn`
6. Error thrown



### Question 3

```python
name = "hello"
name_size = len(name - 1)
print(name_size % 3)
```

1. `0`
2. `1`
3. `2`
4. `3`
5. `4`
6. Error thrown

-->



## Class overview

- Peer instruction
- Exercises
- Halfway through. Students sharing code
- Continue exercises



**Topics**

- Calling functions
  - Argument (input)
  - return
  - Examples
    - `len`
    - `type(true)`
- Creating your own function
  - Parameter
  - Function body
  - return (optional)
  - Calling homemade function
- While loop
  - Test condition
  - Loop body
  - Loop table
- For loop
  - Each character in a string
  - range
- Scope



## Exercises



**Function**

- 6.2.1

- 6.2.2

- 6.3

- Create a function called `getCircleArea`. It should have the `radius` of the circle as parameter and return the circle area. What happens if we dont return anything in the function?

- Write a method that as a parameter gets a number. It should then print to the console if the number is negative, positive or zero

- Write a program that replaces all spaces with 👏 and makes the text uppercase.

  ```
  I am happy today
  I👏AM👏HAPPY👏TODAY
  ```

**Loop**

- 6.4.1
- 6.4.2
- 6.4.3
- Use a loop to print the numbers starting from 5 to -5
- Print a random number of hashtags (`#`) 



### Level 2



#### Exercise 1

Define a function which counts and prints vowels and consonant in a word.



#### Exercise 1.2

Write a python method to find the smallest number among three numbers. The number should come from a user inputting 3 numbers



#### Exercise 2

Write a method to find the middle character of a string. The method should take a string as parameter

```python
middleCharacter = getMiddleCharacter("benjamin"); 
print(middleCharacter); # j
```



#### Exercise 3

Write a java method to calculate the area of a triangle. It should take 3 sides as parameter.

Expected Output:

```
Input Side-1: 10                                                                               
Input Side-2: 15                                                                               
Input Side-3: 20                                                                              
The area of the triangle is 72.6184377413890
```



#### Exercise 4

Lav en metode ved navn printNumbers som tager et naturligt tal, maximum, som argument og skriver tallene fra 1 til og med maximum i firkantede paranteser. For eksempel skal metoden håndtere disse kald:

```python
printNumbers(15);
printNumbers(5);
```

og producere følgende output:

```
[1][2][3][4][5][6][7][8][9][10][11][12][13][14][15]
[1][2][3][4][5]
```



#### Exercise 5

Calculate the sum of digits of a number given by user.

Fx

```python
sum1 = getSumOfNumbers(123)
print(sum1) # 6

sum2 = getSumOfNumbers(12345)
print(sum2) # 15
```



#### Exercise 6

6.5



#### Exercise 7 - Fizz buzz

First ask the user to specify two numbers `start` and `end`

Write a Python method which iterates the integers from `start` to `end`. For  multiples of three print "Fizz" instead of the number and for the  multiples of five print "Buzz". For numbers which are multiples of both  three and five print "FizzBuzz".

```python
start = 10
end = 16
fizzBuzz(start, end)
# Buzz
# 11
# Fizz
# 13
# 14
# Fizz Buzz
# 16
```



##### User defines multiples

Now instead of fizz being printede when multiples of 3 and buzz being printed when multiples of 5. Let the user decide what multiples should be printed for fizz and buzz. fx

```python
start = 10
end = 16
fizzMultiple = 4
buzzMultiple = 6
fizzBuzz(start, end, fizzMultiple, buzzMultiple)
# 10
# 11
# Fizz Buzz
# 13
# 14
# 15
# Fizz
```

*Hint: use modulus for this exercise*



## Project for next class

[Methods project](../projects/methods-project.md)



## Before next class

Check if you are ready with this quiz:https://realpython.com/quizzes/pybasics-functions-loops/