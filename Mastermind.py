import random

# Function to check whether the each of the 4 fruits that player guessed is part of the fruits list
def check_in_list(guess_list, fruits_list):
    in_list = True
    check_list = []
    for fruits in guess_list:                  # For loop to check whether each fruit is in the guess_list
        if fruits in fruits_list:
            check_list.append(True)            # It adds True to the check_list if the fruit is in the fruits_List
        else:
            check_list.append(False)           # It adds False to the check_list if the fruits is not in the fruits_list
    check = all(check_list)                    # If there is one or more false in the list, check will be False. If it is all True, check will be True
    if check is True:
        in_list = True                         # in_list will be True if check is True
    else:
        in_list = False                        # in_list will be False if check is False
    return in_list                             # Shows the result of in_list which is either True or False based on whether there are invalid fruits

# Function for generating the list for player to guess
def randomize_list ():
    for i in range(4):
        final_list.append(random.choice(fruits_list))

# List of fruit available
fruits_list = ['apple', 'orange', 'banana', 'pear', 'lemon', 'grape', 'strawberry']

correct_pos = 0
wrong_pos = 0
# Print the menu and instruction screen
print("-------------------------------------------------------------------------------------------------------------------")
print("Welcome to fruits mastermind game!")
print("-------------------------------------------------------------------------------------------------------------------")
print("*Instruction*")
print("1. You will be required to guess 4 fruits in the correct order from the following list")
print("      ",fruits_list)
print("2. There may be more than one fruits in list")
print("3. Please leave a space between each fruit when giving the answer")
print("   example: pear banana lemon grape")
print("4. You can just enter 'stop' during the game if you want to stop playing")
print("5. The computer will also show number of correct fruits in wrong and correct position as a hint")
print("6. Lastly, have fun!")
print("-------------------------------------------------------------------------------------------------------------------")
print("Enter 1 to start")
print('Enter 2 to exit')

# sentinel value for while loop
game_start = True
game_unfinished = True
attempts = 0
# Empty list for computer to add in the fruits
final_list = []
# Randomize and putting 4 fruits into a list for player to guess
randomize_list()
guess_list = []

# while loop to make sure the player enter the correct command to start or exit
while game_start:
    game_unfinished = True
    print("-------------------------------------------------------------------------------------------------------------------")
    a = int(input())
    print("-------------------------------------------------------------------------------------------------------------------")
    # While loop so if the player guesses wrong, it will allow them to answer again and +1 to their attempts. It also allows them to play again
    while game_unfinished:
        correct_pos = 0
        wrong_pos = 0
        # If player answers 2, it will exit the game for them
        if a == 2:
            print("-------------------------------------------------------------------------------------------------------------------")
            print("Thanks for playing")
            print("-------------------------------------------------------------------------------------------------------------------")
            game_start = False
            game_unfinished = False
        # If player answers 1, the game will start
        elif a == 1:
            game_start = False
            print("List of fruits available:")
            print(fruits_list)
            print("attempts:", attempts)
            print("-------------------------------------------------------------------------------------------------------------------")
            print("|Enter the order below|")
            input_guess = input().lower()
            # If statement for if the player enters 'stop', it will stop the game
            if input_guess == "stop":
                print("-------------------------------------------------------------------------------------------------------------------")
                print("The answer is", final_list)
                print("Number of attempts:", attempts)
                print('Thank you for playing')
                print("-------------------------------------------------------------------------------------------------------------------")
                break
            attempts += 1
            # Splits the player's guess into elements for checking
            guess_list = input_guess.split(" ")
            # If statement to check whether player has answered 4 fruits or not
            if len(guess_list) != len(final_list):
                print("-------------------------------------------------------------------------------------------------------------------")
                print("Invalid answer, please only answer four fruits.")
                print("-------------------------------------------------------------------------------------------------------------------")
                #attempts -= 1
                continue
            # If not statement to check whether the fruits that player has answered are in the fruits list
            if not check_in_list(guess_list, fruits_list):
                print("-------------------------------------------------------------------------------------------------------------------")
                print("Invalid answer, only fruits from the fruits list can be used")
                print("-------------------------------------------------------------------------------------------------------------------")
                #attempts -= 1
                continue
            # Make another list for checking
            final_list_check = []
            final_list_check.extend(final_list)
            guess_list_check = []
            guess_list_check.extend(guess_list)
            # Change those are matched already to a different word so it won't be detected for the wrong position function
            for i in range(4):
                if guess_list_check[i] == final_list_check[i]:
                    correct_pos += 1
                    guess_list_check[i] = "duplicate1"
                    final_list_check[i] = "duplicate2"
            # Check if there are correct fruits but in wrong position
            for i in range(4):
                if guess_list_check[i] != final_list_check[i] and guess_list_check[i] in final_list_check :
                    wrong_pos += 1
            # If they did not answer 4 correctly, it prints how many correct fruits are in the correct position and correct fruits in the wrong position.
            # Then it brings them back through while loop for them to answer the question again
            if correct_pos < 4:
                print("-------------------------------------------------------------------------------------------------------------------")
                print("please try again")
                print("Correct fruits in the correct position:", correct_pos)
                print("Correct fruits but in the wrong position:", wrong_pos)
                print("-------------------------------------------------------------------------------------------------------------------")
            # If all 4 are correct fruits in the correct position, it means they won
            if correct_pos == 4:
                print("-------------------------------------------------------------------------------------------------------------------")
                print("You guessed it right!")
                print("You win!")
                print("Number of attempts:", attempts)
                print("-------------------------------------------------------------------------------------------------------------------")
                confirm_playagain = True
                # While loop to see if the player wants to play again
                while confirm_playagain:
                    print("Would you like to play again?")
                    playagain = str(input("Enter 'yes' to play again. Enter 'no' to quit \n"))
                    # If they type yes, it loops back to the after 'if game_unfinished' and starts a new game
                    if playagain == "yes":
                        confirm_playagain = False
                        attempts = 0
                        print("-------------------------------------------------------------------------------------------------------------------")
                        print("Continuing game...")
                        final_list = []
                        randomize_list()
                        print("Choosing a new order...")
                        print("-------------------------------------------------------------------------------------------------------------------")
                    # If they type no, the loop will be broken and stops the game
                    elif playagain == "no":
                        confirm_playagain = False
                        print("-------------------------------------------------------------------------------------------------------------------")
                        print("Thank you for playing")
                        print("We hope to see you again")
                        print("-------------------------------------------------------------------------------------------------------------------")
                        game_unfinished = False
                    # If they type anything else then 'no' or yes, they will be loop back to answer 'yes' or 'no'
                    else:
                        print("-------------------------------------------------------------------------------------------------------------------")
                        print("Invalid command, please only type 'yes' or 'no'")
                        print("-------------------------------------------------------------------------------------------------------------------")
        # Else statement. If player answers any number other than '1' or '2', the command will be invalid and while loop will bring them back to type the command again
        else:
            print("invalid command, please only type '1' or '2'")
            game_unfinished = False

