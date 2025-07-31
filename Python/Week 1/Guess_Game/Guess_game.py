
def show_levels():
    print("Plase enter level( Easy , Meduim , hard )")


def game_level_choice():
    levels=['Easy','Hard','Meduim']
    while True:
        level=input("Level : ").capitalize()
        if level in levels:
            break
        print("Please enter valid level")
    return level

# Set the game settings according to the game level:
def set_game_settings(game_level):
    ntrial=0
    limits=0
    if game_level =='Easy':
        limits=[1,10]
        ntrial=3
    elif game_level=='Meduim':
        limits=[1,100]
        ntrial=7
    else:
        limits=[1,1000]
        ntrial=15
    return limits,ntrial


from random import randint
def start_play(limits, n_trials):
    c=0
    print(f"Welcomme Guess game please enter number between {limits[0]} and {limits[1]}")
    rand=randint(limits[0],limits[1])
    while True:
        num=int(input("NUmber : "))
        if num == rand:
            print('Congratulations')
            break
        else:
            if c==n_trials:
                print(f'You Lose! the Number is {rand}')
                break
            if num>rand:
                print("Decrease")
            elif num<rand:
                print("Increase")
            c+=1

def play():
    show_levels()
    game_level = game_level_choice()
    limits, n_trials = set_game_settings(game_level)
    start_play(limits, n_trials)

if __name__=='__main__':
    play()