def play_21_game():
    current_number = 0  # Start the count at 0
    player_turn = 1     # Player 1 starts the game
    
    while current_number < 21:
        print(f"Player {player_turn}'s turn.")
        
        # Ask the player to choose how many numbers they want to say
        player_choice = int(input("How many numbers do you want to say (1, 2, or 3)? "))
        
        # Ensure the player chooses a valid number (1, 2, or 3)
        if player_choice not in [1, 2, 3]:
            print("Invalid choice! You can only say 1, 2, or 3 numbers.")
            continue  # Ask the player again
        
        # Update the current number
        current_number += player_choice
        print(f"Current number is: {current_number}")
        
        # Check if the game is over
        if current_number >= 21:
            print(f"Player {player_turn} said 21! Player {player_turn} loses!")
            break
        
        # Switch turns: if player_turn is 1, switch to 2, and vice versa
        player_turn = 2 if player_turn == 1 else 1

# Call the game function to start playing
play_21_game()
