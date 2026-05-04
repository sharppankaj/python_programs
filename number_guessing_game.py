# Number guessing game

import random


print("Welcome to Number guessing game!!")

low = int(input("Enter the lower bound:"))
high = int(input("Enter the upper bound:"))

print(f"You have 5 chances to guess it. Lets start!!")

num = random.randint(low, high)  # Randmon number generator

ch = 5
gc = 0

while gc < ch:
    gc += 1
    guess = int(input(f"Attempt{gc}/{ch}. Enter your guess:"))

    if guess == num:
        print(f"Congratulations! You guessed it correctly in {gc} attempts.")
        break

    elif guess < num and guess >= low:
        print("Your guess is too low. Try again!")

    elif guess > num and guess <= high:
        print("Your guess is too high. Try again.")

    elif guess >= ch and guess != num:
        print(f"Sorry! The number is {num}. Better luck next time.")
