# dicegame
import random

print("THE ULTIMATE DICE GAME")
player_name = input("Enter your name: ")
print('Type "help".')
options = (1, 2, 3, 4, 5, 6)
gameEnd = False
playerBet = False
player_money = 100
bet_amount = 0

while not gameEnd:
    player_choice = input(">")

    # getting help
    if player_choice.lower() == "help":
        print("bet - to bet")
        print("roll - to roll the dice")
        print("leave - to leave the game")
        print("balance - to check your balance")

    # betting
    elif player_choice.lower() == "bet":

        bet_amount = int(input("How much do you want to bet? "))
        if bet_amount > player_money:
            print("You don't have that much money.")
        elif bet_amount <= player_money and not playerBet:
            playerBet = True
            print(f"You bet {bet_amount} and COMP matched it. ${bet_amount * 2} is on the line!")
        elif playerBet:
            print("You've already placed a bet.")

    # rolling the dice
    elif player_choice.lower() == "roll":
        playerBet = False
        random_dice = random.choice(options)
        print(f"You rolled a {random_dice}")
        print("Now it's COMP's turn.")
        random_dice_comp = random.choice(options)
        print(f"COMP rolled a {random_dice_comp}")

        if random_dice > random_dice_comp:
            print(f"{player_name.capitalize()} won!")
            player_money += bet_amount

        elif random_dice < random_dice_comp:
            player_money -= bet_amount
            print("COMP won!")
            if player_money == 0:
                gameEnd = True
                print("You've lost all your money.")

        else:
            player_money += bet_amount
            print("It's a tie!")

    # checking balance
    elif player_choice.lower() == "balance" or player_choice.lower() == "bal":
        print(f"You have ${player_money}.")

    # leaving the game
    elif player_choice.lower() == "leave" or player_choice.lower() == "exit":
        exit_trigger = input("Are you sure you want to exit? (yes/no) ")
        if exit_trigger.lower() == "yes":
            gameEnd = True
            print("Exiting the game.")
        elif exit_trigger.lower() == "no":
            print("Resuming.")
        else:
            print("I can't understand that.")

    # incorrect input
    else:
        print("I can't understand that.")


