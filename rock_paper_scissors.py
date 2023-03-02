import random

exit = False


while exit == False:
    option = ["rock", "paper", "scissors"]
    user_option = input("Choose Rock, Paper, Scissors or Exit: ")
    computer_option = random.choice(option)

    if user_option == "exit":
        print("Game over!")
        exit = True
        
    elif user_option == "rock":
        if computer_option == "rock":
            print("Computer chose Rock")
            print("It's a tie!")
        elif computer_option == "paper":
            print("Computer chose Paper")
            print("Computer won!")
        else:
            print("Computer chose Scissors")
            print("You won!")
            
    elif user_option == "paper":
        if computer_option == "rock":
            print("Computer chose Rock")
            print("You won!")
        elif computer_option == "paper":
            print("Computer chose Paper")
            print("It's a tie!")
        else:
            print("Computer chose Scissors")
            print("Computer won!")

    else:
        if computer_option == "rock":
            print("Computer chose Rock")
            print("Computer won!")
        elif computer_option == "paper":
            print("Computer chose Paper")
            print("You won!")
        else:
            print("Computer chose Scissors")
            print("It's a tie!")
            