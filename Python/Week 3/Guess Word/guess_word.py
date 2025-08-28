from random import choice

def Message():
    print("Welcome in Guess Word")

def Choice_Level():
    print("PLease enter Level\n - Easy\n - Meduim\n - Hard")
    levels = {'Easy': 15, 'Medium': 10, 'Hard': 6}
    while True:
        level=input("Level : ").capitalize()
        if level in levels:
            return levels[level]
        print('Please enter Valid Level')

def Choice_word():
    print("Choose a category:\n - Animal\n - City\n - Food\n - Job\n - Nation")
    dic={
        "Animal" : ['Cat','Dog','Lion','Elephant','Zebra','Monkey','Dolphin','Tiger','Giraffe','Bear','Kangaroo','Crocodile','Horse','Panda','Wolf','Fox','Deer','Rabbit','Owl','Camel','Shark','Penguin'],
        'City' : ['Cairo','Paris','Tokyo','New York','Sydney','London','Dubai','Rome','Berlin','Toronto','Istanbul','Beijing','Madrid','Buenos Aires','Moscow','Athens','Los Angeles','Chicago','Seoul','Bangkok'],
        'Food' : ['Pizza' , 'Rice', 'Chicken', 'Burger', 'Pasta', 'Sushi', 'Salad', 'Sandwich', 'Steak', 'Ice cream', 'Tacos','Fruits','Soup','Noodles','Cake','Curry','Bread','Chocolate','Fries','Dumplings' ],
        'Job' : ['Engineer' , 'Doctor', 'Teacher', 'Chef', 'Pilot', 'Artist', 'Accountant', 'Lawyer', 'Nurse', 'Mechanic','Scientist','Dentist','Firefighter','Pharmacist','Driver','Plumber','Electrician','Photographer','Architect'],
        'Nation' : ['Egypt' , 'France', 'Japan', 'Brazil', 'Canada', 'India', 'China', 'Germany', 'Mexico', 'South Africa','Russia','Spain','Italy','Argentina','Nigeria','Thailand','Turkey','Sweden','Norway','Pakistan']
    }
    while True:
        ch=input("Your Choice : ").title()
        if ch in dic.keys():
            print("Word Selected")
            return choice(dic[ch])
        print("please enter valid choice")

def Show_Word(word,lis_word):

    result=[]
    for i, ch in enumerate(word):
        if  lis_word.count(ch) > word[:i+1].count(ch)-1:
            result.append(ch)
        else:
            result.append('-')
    print("Word:", ''.join(result))


def take_input(word,lis_word,ntime):
    while True:
        if ntime==0:
            return 0
        letter=input("Letter : ")
        if (letter in word and letter not in lis_word) or (word.count(letter) != lis_word.count(letter)):
            print("#"*50)
            print("Correct guess")
            lis_word.append(letter)
            return ntime
        elif len(letter)!=1:
            print(f'Please Enter single Letter | Attempts left: {ntime-1}')
        else:
            print(f"Please enter valid Letter | Attempts left: {ntime-1}")
        ntime-=1



def play():
    Message()
    ntime=Choice_Level()
    word=Choice_word()
    lis_word=[]
    while True:
        Show_Word(word,lis_word)
        print(f"Attempts left: {ntime}")
        ntime=take_input(word,lis_word,ntime)
        if ntime==0 :
            print(f'You are lose the word : {word}')
            return
        if len(word) ==len(lis_word):
            print(f"You won! The word was: {word}")
            return
        

if __name__=='__main__':
    play()

