import random

def playGame():
    print("Welcome to the Rock-Paper-Scissors game......")

    def getBotChoice():
        listOfChoices4Bot = ["rock", "paper", "scissors", "chad", "rock", "paper", "scissors"]
        return listOfChoices4Bot[random.randint(0,3)]

    def getUserChoice():
        result = ""
        while True:
            listOfChoices = ["rock", "paper", "scissors", "q"]
            Userinput = input("Choose your hand by typing 'scissors', 'rock', or 'paper' -- choose wisely : ").lower()
            if listOfChoices.__contains__(Userinput):
                result = Userinput
                break
            print("Please choose again, that is not one of the possible hands")
        return result

    while True:
        humanScore = 0
        botScore = 0

        userChoice = getUserChoice()
        botChoice = getBotChoice()
        if userChoice == "q":
            print("I see. You have chosen to quit. What a loser. Come back when you have some courage")
            break

        print(f"You chose {userChoice}, while I chose {botChoice}")

        if botChoice == "chad":
            print("Unfortunately for you, I have luckily drawn an ultra rare 'Chad' hand. There is no way to beat it.")
            print("You have lost this round")
            botScore +=1
        elif userChoice == botChoice:
            print("We have drawn this round")
        elif userChoice == "scissors":
            if botChoice == "paper":
                print("You have won this round")
                humanScore +=1
            else:
                print("You have lost this round")
                botScore += 1
        elif userChoice == "paper":
            if botChoice == "rock":
                print("You have won this round")
                humanScore +=1
            else:
                print("You have lost this round")
                botScore += 1
        elif userChoice == "rock":
            if botChoice == "scissors":
                print("You have won this round")
                humanScore += 1
            else:
                print("You have lost this round")
                botScore += 1
        print("--------------------------------------")
        print("The current score : ")
        print(f"You have {humanScore} wins ")
        print(f"I have {botScore} wins")
        print("--------------------------------------")
        print("to quit at any time -  type 'q'")
        print("OK lets play another round")


def main():
    playGame()
main()