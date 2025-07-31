
PIN = "1234"                # Default user PIN
balance = 1000.0            # Default account balance (USD)
transactions = []           # List to store last transactions
li=["Balance inquiry" , "Deposit" , 'Withdraw', 'Mini statement' , 'Exit']



def authenticate():
    '''
    Requests user to enter the PIN up to 3 times.
    Returns True if successful, False otherwise.
    '''
    for i in range(3):
        enter_pin=input("PIN : ")
        if enter_pin==PIN:
            return True
        print("Not vailed PIN")
    return False



def show_menu():
    '''
    Shows the ATM options to the user.
    '''
    print("\nAvailable Transactions :")

    print(" - Balance inquiry ")
    print(" - Deposit")
    print(" - Withdraw")
    print(" - Mini statement")
    print(" - Exit")


def balance_inquiry():
    '''
    Prints the current balance.
    '''
    print(f"Current Account Balance : {balance}")



def deposit():
    '''
    Lets the user deposit an amount.
    Updates balance and transaction history.
    '''
    global balance
    while True:
        n=int(input("Number of Deposit : "))
        if n>0:
            balance+=n
            print("Vallied Transection")
            break
        print("Enter postive Number : ")


def withdraw():
    '''
    Lets the user withdraw an amount.
    Checks for valid and sufficient balance.
    Updates transaction history.
    '''
    global balance
    while True:
        n=int(input("Number of Withdraw : "))
        if balance>n :
            balance-=n
            print("Valied transection")
            return
        print("ENter vailled Withdraw")



def mini_statement():
    '''
    Prints the last 5 transactions.
    '''
    if len(transactions)>=5:
        for i in range(-1,-6,-1):
            print(transactions[i])
    else:
        for i in transactions:
            print(i)


def main():
    '''
    Main program loop: authentication and operations.
    '''
    if authenticate():
        while True:
            show_menu()
            while True:
                n=input("Enter transectoin : ").capitalize().strip()
                if n in li:
                    transactions.append(n)
                    break
                print("Please enter valid transection ")
            if n=="Balance inquiry":
                balance_inquiry()
            elif n=='Deposit':
                deposit()
            elif n=='Withdraw':
                withdraw()
            elif n=='Mini statement':
                mini_statement()
            elif n=='Exit':
                return
            print("-"*50)

if __name__=='__main__':
    main()