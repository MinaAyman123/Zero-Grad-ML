def Welcomme_Message():
    print("Welcomme in Prime Numbers Dictionary")

def isPrime(num):
    if num==1:
        return False
    for i in range(2,num):
        if num %i==0:
            return False
    return True

def Generate_dictonary(limit):
    dic={}
    count=1
    for i in range(1,limit+1):
        if isPrime(i):
            dic[count]=i
            count+=1
    return dic

def display_prime(prime_dictonary : dict):
    for key,value in prime_dictonary.items():
        print(f"{key} -> {value}")

def display_number(prime_dictonary,postion):
    try:
        return prime_dictonary[postion]
    except KeyError:
        print("Invaliied Postion")


def display_Menu():
    print("""Menu:
Enter 1 to View all primes
enter 2 to  Get prime by position
enter 3 to Exit
""")


def take_input():
    lis=[1,2,3]
    while True:
        option=int(input("Choose"))
        if option in lis:
            return option
        print("invallied Option")


def play():
    Welcomme_Message()
    num=int(input("Number : "))
    dictionary_prime=Generate_dictonary(num)
    while True:
        display_Menu()
        option=take_input()
        if option==1:
            display_prime(dictionary_prime)
        elif option==2:
            postion=int(input("Postion :"))
            print(display_number(dictionary_prime,postion))
        else:
            break
        print("-"*100)


if __name__=='__main__':
    play()