import random
import time
print("Welcome to Number Guessing Game.")
    # Variables
TheNumber = random.randint(1,50)
lives = 3
attempts = 0
    # Main File
while True:
    try:
        lives = int(input("How many lives do you want (between 1 and 50): "))
        if 1 <= lives <= 50: # same as lives >= 1 and lives <= 50
            break
        else:
            print("Try again, Enter a number between 1 and 50.")
    except ValueError:
        print("Try again, Enter a valid number.")



print("Generating A Number.... ")
time.sleep(3)
print("Number Generated ....")
while lives!=0:
    while True:
        try:
            UserInput = int(input("Enter your Number to Guess.\n: "))
            if UserInput >=1 and UserInput <= 50:
                break
            else:
                print("Babeo Number Deynai 50 or 1 ke darmiyaan. Chawlian marne nu nhi kaha.")
        except ValueError:
            print("Number not Bs. ")
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