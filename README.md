# Python-project-Guess-the-number

Project: Guess the number game

This project will allow the user to guess a randomly generated number between 1 and 100.

Step 1: Open a Python editor

To begin, you'll need to open a Python editor. There are several options available, including IDLE, PyCharm, and Visual Studio Code. For this project, we'll be using IDLE, which is a simple and user-friendly editor that comes bundled with Python.

Step 2: Create a new Python file

Once you have your editor open, create a new Python file by selecting "File" -> "New File" from the menu. This will open a blank file where you can write your code.

Step 3: Import the random module

The random module in Python allows you to generate random numbers. To use this module, you'll need to import it at the beginning of your code. Add the following line of code to your file:

import random


Step 4: Generate a random number

Next, you'll need to generate a random number between 1 and 100. You can do this using the randint() function from the random module. Add the following line of code to your file:


number = random.randint(1, 100)

This will generate a random number and store it in the variable "number".

Step 5: Get the user's guess

Now, you'll need to get the user's guess. You can do this using the input() function in Python, which allows the user to enter text. Add the following line of code to your file:



guess = int(input("Guess a number between 1 and 100: "))
This will prompt the user to enter a number between 1 and 100 and store their guess in the variable "guess".

Step 6: Compare the guess to the number

Next, you'll need to compare the user's guess to the random number. You can do this using an if statement in Python. Add the following lines of code to your file:


if guess == number:
    print("Congratulations! You guessed the number.")
elif guess < number:
    print("Your guess is too low. Try again.")
else:
    print("Your guess is too high. Try again.")
    
    
This code will check if the user's guess is equal to the random number, and if so, it will print a congratulatory message. If the guess is too low or too high, it will prompt the user to try again.

Step 7: Add a loop

Finally, you'll want to add a loop that allows the user to keep guessing until they get the right answer. Add the following lines of code to your file:


while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        print("Congratulations! You guessed the number.")
    elif guess < number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
        
This code will keep prompting the user to guess until they get the right answer.

Step 8: Save and run your code

Once you've completed the above steps, save your code by selecting "File" -> "Save" from the menu. Choose a filename and save your file with a .py extension (e.g. guess_the_number.py).

To run your code, select "Run" -> "Run Module" from the menu. This will execute your code and allow you to play the game.

That's it
