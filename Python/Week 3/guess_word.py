from random import choice
nTrail=10

def Choice_Word():
    return choice(['Mina','Bab','Gdo'])

def display_Word(word,Letter_list):
    for letter in word:
        if letter in Letter_list:
            print(letter,end='')
        else:
            print('-',end='')
    print()

def guess_validation(letter_list,trial, word):
        while True:
            letter=input("Please enter Single Letter : ")
            if len(letter)==1 and letter not in letter_list and letter in word:
                letter_list.append(letter)
                return trial
            trial+=1
            if trial==nTrail:
                return "Lost the Game"
            print("Please Aenter one letter")

def play():
    word=Choice_Word()
    letter_li=[]
    trial=0
    while True:
        trial=guess_validation(letter_li,trial,word)
        if trial=='Lost the Game':
            print(f"Lost the Game the Word {word}")
            return
        display_Word(word,letter_li)

play()

