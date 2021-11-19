# Week 47 - Strings and if else



## Todays program

- Feedback on Crypto converter

- What is a string

- Using input

  - Compare with Java

  - ```java
    import java.util.Scanner;  // Import the Scanner class
    class Main {
      public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        String text = myObj.nextLine();
        System.out.println(text);
      }
    }
    ```

  - 

- Escaping, multiline (press enter ) and paragraphs `"""` (prints the new line)

- Index and length

- Concatenation
  - Convert int to number and number to int

- String methods in groups
  - `slice`
  - `lower`
  - `upper`
  - `rstrip`
  - `lstrip`
  - `strip`
  - contains using `in`

- if else sentence





## Feedback on Crypto Converter

- Really well done! 
  - good variable names
  - cleary understanding what i taught yesterday
  - really Nice with `round`
- Good structure with 
  - first defining global stuff
  - Calculating then printing
- `print(f"For {amount_spend}$ you can get")`
- Missing comments



## Exercises



### Exercise 1

In groups of two find a partner group. Then with the partner group decide what group takes what topic. Now investigate what the methods below does? Create some code showing how to use the method in a program

- `startswith` and `find`
- `replace` and `endswith`



1. Spend 10 minutes investigating in your group
2. Spend 10 minutes presenting



---

### Exercises - level 1

Level 1 will get you up to speed with working with the 

Do the following exercises from the book 👇

- 4.1.1
- Create a multiline print statement
- 4.2.1
- 4.2.2
- 4.2.4
- 4.3.1
- 4.3.3
- 4.3.4
- 4.4.1
- 4.6.4



### Exercise 2

Create a variable with your name. If your name contains the character `e` then log out the string `YOUR_NAME contains e`. If not the log out `YOUR_NAME does not contain e`. 



### Exercises - level 2

These exercises are a bit more open ended and not everything have been taught. So you will need to research for yourself!



### L33t H4x0r

- 4.9



### Valid password

Let a user input his/her password. Now we have to figure out if the password is valid. There are the rules:

- Must be longer than 8 characters
- Cannot contain the word password
- Has to have a special character
- Must not start with a number

*Hint: look into the `and` operator*



#### Password score

Figure out a way to score how complicated the password is. You have to come up with the formula. A super simple method would be just to score based on the length of the password. Based on the score print something to the user

Example of the code

```
Welcome to this password checker. What is your password?
monkey123_
monkey123_ is a valid passsword. It's score is 234. That makes the password good
```



### Valid email

Write a program that checks if an email is valid. Off course the `@` you have to check for. But what if a user does not write a domain fx. 

*Hint: this can be a gigantuan task. So scope it*





## Project for next week

[String analyzer and BMI calculator](../projects/string-analyzer-bmi.md)



## Before next class

Check if you are ready with this quiz: https://realpython.com/quizzes/pybasics-strings/