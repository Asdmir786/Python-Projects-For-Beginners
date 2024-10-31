import random
import time
print("Welcome to Number Guessing Game.")
    # Variables
TheNumber = random.randint(1,50)
lives = 3
attempts = 0
    # Main File
while True:
    lives = int(input("How many Lives Do you want. "))
    if lives < 50 and lives > 0:
        break
    else:
        print("Enter a Number Which is lower than 50. ")


print("Generating A Number.... ")
time.sleep(3)
print("Number Generated ....")
while lives!=0:
    UserInput = int(input("Enter your Number to Guess.\n: "))
    attempts += 1
    if UserInput == TheNumber:
        print(f"You Guessed the Number {TheNumber} in {attempts} attempts and {lives} left.")
        break
    elif UserInput > TheNumber:
        lives -= 1
        print(f"Your Number is Too High, Try Again. ({lives} lives left.)\n")
    elif UserInput < TheNumber:
        lives -= 1
        print(f"Your Number is Too Low, Try Again. ({lives} lives left.)\n")
    else: 
        print("Enter a Number Only.\n")

    if lives == 0:
        print(f"Nice Try, The Number was {TheNumber}.")
        time.sleep(5)

print("Game Ended.")