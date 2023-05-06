Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... number = random.randint(1, 100)
... guess = int(input("Guess a number between 1 and 100: "))
... 
... if guess == number:
...     print("Congratulations! You guessed the number.")
... elif guess < number:
...     print("Your guess is too low. Try again.")
... else:
...     print("Your guess is too high. Try again.")
... 
... while guess != number:
...     guess = int(input("Guess a number between 1 and 100: "))
...     if guess == number:
...         print("Congratulations! You guessed the number.")
...     elif guess < number:
...         print("Your guess is too low. Try again.")
...     else:
...         print("Your guess is too high. Try again.")
