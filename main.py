#The game has three choices: Rock, Paper, and Scissors.
#Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.
#A tie occurs if both players choose the same option.
import random

def rock_paper_scissors():
    score = {"wins": 0, "losses": 0, "ties": 0}  # Score tracker
    overallScore = score["wins"] + score["losses"] + score["ties"]
    while True:
        print("Please choose an option from 1-4")
        print("\n1. Play one game")
        print("\n2 Play first to 10 wins")
        print("\n3. Check your score")
        print("\n4. Exit the game...")
        choice = input("Enter your choice: 1-4: ")
    
        if choice == "1":
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"You chose {user_choice}, computer chose {computer_choice}.")
            if user_choice == computer_choice:
                    print("It's a tie!")
                    score["ties"] += 1
            elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                    (user_choice == "Paper" and computer_choice == "Rock") or \
                    (user_choice == "Scissors" and computer_choice == "Paper"):
                    print("You win!")
                    score["wins"] += 1
            else:
                    print("You lose!")
                    score["losses"] += 1
        elif choice == "2":
            while score["wins"] <= 10:
                user_choice = get_user_choice()
                computer_choice = get_computer_choice()
            
                print(f"You chose {user_choice}, computer chose {computer_choice}.")
                if user_choice == computer_choice:
                    print("It's a tie!")
                    score["ties"] += 1
                elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                    (user_choice == "Paper" and computer_choice == "Rock") or \
                    (user_choice == "Scissors" and computer_choice == "Paper"):
                    print("You win!")
                    score["wins"] += 1
                else:
                    print("You lose!")
                    score["losses"] += 1
        elif choice == "3":
            print(f"Score: {score['wins']} Wins, {score['losses']} Losses, {score['ties']} Ties")
        elif choice == "4":
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

            
            
def get_user_choice():
    choice_map = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    print("Choose your weapon!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    weapon = input("Enter your choice 1-3: ")
    if weapon in choice_map:
        return choice_map[weapon]
    else:
        print("Invalid choice. Please try again.")
    return get_user_choice()
    

def get_computer_choice():
    weapon_choices = ["Rock", "Paper", "Scissors"]
        
    return random.choice(weapon_choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
     (user_choice == "Paper" and computer_choice == "Rock") or \
     (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("You lose!")

    
def main() :
    rock_paper_scissors()
 
#Doesnt run the main function unless we choose an option 
if __name__ == "__main__":
    main()
    

    

    

    
    
