import time
import random

words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xigua", "yam", "zucchini", "ant", "bee", "cat", "dog", "elephant", "fox",
    "giraffe", "hippo", "iguana", "jaguar", "kangaroo", "lion", "monkey", "narwhal", "owl", "penguin",
    "quail", "rabbit", "snake", "tiger", "urchin", "vulture", "wolf", "xerus", "yak", "zebra",
    "airplane", "boat", "car", "drone", "elevator", "ferry", "gondola", "helicopter", "icebreaker", "jet",
    "kayak", "launch", "motorcycle", "narrowboat", "oceanliner", "paraglider", "quad", "rocket", "scooter", "tank",
    "unicycle", "van", "wagon", "yacht", "zeppelin", "book", "chair", "desk", "envelope", "fan",
    "glasses", "hat", "ink", "jug", "key", "lamp", "mirror", "notebook", "oven", "pencil",
    "quilt", "rug", "stool", "table", "umbrella", "vase", "window", "xylophone", "yarn", "zipper"
]
RandomWordWhichIsChoosen = random.choice(words)
attempts = 0

print("Welcome to Guess The Bloody Word, which are all english words (mostly).")
print("Random Word Choosing ....")
time.sleep(3)
print("Selected!")
time.sleep(1)
while True:
    try:
        lives = int(input("How many lives do you want (between 1 and 50): "))
        if 1 <= lives <= 50: # same as lives >= 1 and lives <= 50
            break
        else:
            print("Try again, Enter a number between 1 and 50.")
    except ValueError:
        print("Try again, Enter a valid number.")

while lives != 0:
    UserWordInput = input(f"Enter The word.({RandomWordWhichIsChoosen})\n: ").strip().lower()
    attempts += 1
    if UserWordInput == RandomWordWhichIsChoosen:
        print(f"YEEEEEEEEE HAAAAAAW, You Guessed the word {RandomWordWhichIsChoosen} with {lives} lives left and in {attempts} attempts.")
        break
    
    elif UserWordInput != RandomWordWhichIsChoosen:
        print(f"Nope")
        lives -= 1
    else:
        print("Chawlian mari ja rha hai tab se ab hil gya hai kya?")
    if lives == 0:
        print(f"Sorry, you've run out of lives! The correct word was '{RandomWordWhichIsChoosen}'.")
print("Kle Khao")