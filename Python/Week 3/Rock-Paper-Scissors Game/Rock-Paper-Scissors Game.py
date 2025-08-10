from random import choice
option=['Rock','Scissors','Paper']

def Welcome_Message():
    print("Welcomme in Rock-Paper-Scissors Game")

def get_user_choice():
    print("Please Choice one of :\n - Rock\n - Scissors\n - Paper ")
    print()
    while True:
        op=input("Your Choice").capitalize().strip()
        if op in option:
            return op
        print("Please enter Valid option")

def get_computer_choice():
    return choice(option)

def determine_winner(user, computer):
    if (user=='Rock' and computer=='Scissors') or (user=='Scissors' and computer=='Paper') or (user=='Paper' and computer=='Rock'):
        return 'Your Win'
    

    elif (user=='Scissors' and computer=='Rock') or (user=='Paper' and computer=='Scissors') or (user=='Rock' and computer=='Paper'):
        return 'Computer Win'
    return "Draw"

def play_game():
    Welcome_Message()
    while True:
        Your_Choice=get_user_choice()
        computer=get_computer_choice()
        print(f"Computer Choicd : {computer}")
        print(determine_winner(Your_Choice,computer))
        print('-'*50)
        com=input("Are you play anther game ? (Yes / No)").capitalize().strip()
        if com=='No':
            break

if __name__=='__main__':
    play_game()