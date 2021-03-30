import random


def play_game():
    print("Welcome to the Rock-Paper-Scissors game......")

    def get_bot_choice():
        list_of_choices_4_bot = ["rock", "paper", "scissors", "chad", "rock", "paper", "scissors"]
        return list_of_choices_4_bot[random.randint(0, 3)]

    def get_user_choice():
        while True:
            list_of_choices = ["rock", "paper", "scissors", "q"]
            user_input = input("Choose your hand by typing 'scissors', 'rock', or 'paper' -- choose wisely : ").lower()
            if list_of_choices.__contains__(user_input):
                return user_input
            print("Please choose again, that is not one of the possible hands")

    human_score = 0
    bot_score = 0
    while True:


        user_choice = get_user_choice()
        bot_choice = get_bot_choice()
        if user_choice == "q":
            print("I see. You have chosen to quit. What a loser. Come back when you have some courage")
            break
        print("--------------------------------------")
        print(f"You chose {user_choice}, while I chose {bot_choice}")

        if bot_choice == "chad":
            print("Unfortunately for you, I have luckily drawn an ultra rare 'Chad' hand. There is no way to beat it.")
            print("You have lost this round")
            bot_score += 1
        elif user_choice == bot_choice:
            print("We have drawn this round")
        elif user_choice == "scissors":
            if bot_choice == "paper":
                print("You have won this round")
                human_score += 1
            else:
                print("You have lost this round")
                bot_score += 1
        elif user_choice == "paper":
            if bot_choice == "rock":
                print("You have won this round")
                human_score += 1
            else:
                print("You have lost this round")
                bot_score += 1
        elif user_choice == "rock":
            if bot_choice == "scissors":
                print("You have won this round")
                human_score += 1
            else:
                print("You have lost this round")
                bot_score += 1
        print("--------------------------------------")
        print(">>>>> The current score : ")
        print(f"You have {human_score} wins ")
        print(f"I have {bot_score} wins")
        print("--------------------------------------")
        print("to quit at any time -  type 'q'")
        print("OK lets play another round")
        print("--------------------------------------")


def main():
    play_game()


main()
