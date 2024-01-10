# This is a slot machine game written in Python
# It demonstrates the use of IPO, variables, constants, decision structures and looping

# Import the random module to generate random numbers
import random

# Define the constants for the game
CREDITS = 100 # The initial amount of credits the player has
BET_CHOICES = [1, 2, 5, 10] # The valid choices for the bet amount
SLOT_ITEMS = ["Cherry", "Lemon", "Lucky 7", "Bar", "Diamond", "Jackpot"] # The possible items for each slot
PRIZES = { # The prizes for each winning combination, based on the player's bet
    "Cherry1": 1, # Only the first slot is a cherry
    "Cherry2": 2, # Cherry in the first two slots
    "Cherry3": 3, # Three cherries
    "Lemon3": 5, # Three lemons
    "Lucky73": 7, # Three lucky 7's
    "Bar3": 10, # Three bars
    "Diamond3": 20, # Three diamonds
    "Jackpot3": "Jackpot" # Three jackpots
}

# Define the variables for the game
jackpot = 0 # The amount of credits in the jackpot
play = True # A flag to indicate whether the player wants to play or quit
hold = [False, False, False] # A list to indicate whether the player wants to hold each slot
hold_count = 0 # A counter to keep track of how many holds the player has used
win_count = 0 # A counter to keep track of how many games the player has won
lose_count = 0 # A counter to keep track of how many games the player has lost

# Define a function to spin the slots and return the result
def spin_slots():
    # Create an empty list to store the result
    result = []
    # Loop through each slot
    for i in range(3):
        # If the slot is not on hold
        if not hold[i]:
            # Generate a random number between 0 and 5
            num = random.randint(0, 5)
            # Append the corresponding item to the result list
            result.append(SLOT_ITEMS[num])
        # If the slot is on hold
        else:
            # Append the previous item to the result list
            result.append(slots[i])
    # Return the result list
    return result

# Define a function to check the result and return the prize
def check_result(result):
    # Create an empty string to store the combination
    combination = ""
    # Loop through each item in the result list
    for item in result:
        # Add the first letter of the item to the combination string
        combination += item[0]
    # If the combination is in the PRIZES dictionary
    if combination in PRIZES:
        # Return the prize value
        return PRIZES[combination]
    # If the combination is not in the PRIZES dictionary
    else:
        # Return zero
        return 0

# Define a function to print the result and the prize
def print_result(result, prize):
    # Print a blank line
    print()
    # Print the result in a formatted way
    print(f"Your spin: {result[0]} | {result[1]} | {result[2]}")
    # If the prize is zero
    if prize == 0:
        # Print a message that the player did not win anything
        print("Sorry, you did not win anything.")
    # If the prize is not zero
    else:
        # If the prize is the jackpot
        if prize == "Jackpot":
            # Print a message that the player won the jackpot
            print(f"Congratulations, you won the jackpot of {jackpot} credits!")
        # If the prize is not the jackpot
        else:
            # Print a message that the player won the prize
            print(f"Congratulations, you won {prize} credits!")
    # Print a blank line
    print()

# Define a function to print the game statistics
def print_stats():
    # Print a blank line
    print()
    # Print the total amount of games won
    print(f"Total games won: {win_count}")
    # Print the total amount of games lost
    print(f"Total games lost: {lose_count}")
    # Print the total amount of credits the player finished with
    print(f"Total credits: {credits}")
    # If the player made more credits than they started with
    if credits > CREDITS:
        # Print a congratulatory message
        print("You did well!")
    # If the player quit with fewer credits than they started with
    elif credits < CREDITS:
        # Print a consolation message
        print("Better luck next time!")
    # If the player quit with the same amount of credits as they started with
    else:
        # Print a neutral message
        print("You broke even!")
    # Print a blank line
    print()

# Print a welcome message
print("Welcome to the slot machine game!")
# Print the initial amount of credits
print(f"You have {credits} credits to start with.")

# Start the main loop
while play:
    # Print a blank line
    print()
    # Prompt the user for how many credits they would like to bet
    bet = int(input("How many credits would you like to bet? (1, 2, 5 or 10) "))
    # Validate the user's input
    while bet not in BET_CHOICES or bet > credits:
        # Print an error message
        print("Invalid bet. Please try again.")
        # Prompt the user again
        bet = int(input("How many credits would you like to bet? (1, 2, 5 or 10) "))
    # Deduct the bet from the total credits
    credits -= bet
    # Add the bet to the jackpot
    jackpot += bet
    # Print the updated amount of credits and jackpot
    print(f"You have {credits} credits left.")
    print(f"The jackpot is {jackpot} credits.")
    # Spin the slots and store the result
    slots = spin_slots()
    # Check the result and store the prize
    prize = check_result(slots)
    # Print the result and the prize
    print_result(slots, prize)
    # If the prize is zero
    if prize == 0:
        # Increment the lose count
        lose_count += 1
        # Ask the user if they want to hold any slots
        hold_choice = input("Do you want to hold any slots? (y/n) ")
        # Validate the user's input
        while hold_choice not in ["y", "n"]:
            # Print an error message
            print("Invalid choice. Please try again.")
            # Ask the user again
            hold_choice = input("Do you want to hold any slots? (y/n) ")
        # If the user wants to hold any slots
        if hold_choice == "y":
            # If the hold count is zero
            if hold_count == 0:
                # Loop through each slot
                for i in range(3):
                    # Ask the user if they want to hold this slot
                    hold[i] = input(f"Do you want to hold slot {i+1}? (y/n) ") == "y"
                # Increment the hold count
                hold_count += 1
            # If the hold count is not zero
            else:
                # Print a message that the user cannot use a hold two spins in a row
                print("Sorry, you cannot use a hold two spins in a row.")
    # If the prize is not zero
    else:
        # Increment the win count
        win_count += 1
        # If the prize is the jackpot
        if prize == "Jackpot":
            # Add the jackpot to the total credits
            credits += jackpot
            # Set the jackpot to zero
            jackpot = 0
        # If the prize is not the jackpot
        else:
            # Add the prize to the total credits
            credits += prize
        # Reset the hold list to False
        hold = [False, False, False]
        # Reset the hold count to zero
        hold_count = 0
    # If the user has no credits left
    if credits == 0:
        # Print a message that the user cannot continue playing
        print("You have no credits left. You cannot continue playing.")
        # Set the play flag to False
        play = False
    # If the user has some credits left
    else:
        # Ask the user if they want to play again or quit
        play_choice = input("Do you want to play again or quit? (p/q) ")

    # Validate the user's input for playing again or quitting
    while play_choice not in ["p", "q"]:
        # Print an error message
        print("Invalid choice. Please try again.")
        # Ask the user again
        play_choice = input("Do you want to play again or quit? (p/q) ")

    # If the user wants to play again
    if play_choice == "p":
        # Print a message indicating the start of a new game
        print("Starting a new game!")
    else:
        # Print the game statistics
        print_stats()
        # Set the play flag to False
        play = False

# End the main loop

# End of the program
