class Atm(object):
    def __init__(self, cardNo, pinNo, money):
        self.cardNo = cardNo
        self.pinNo = pinNo
        self.money = money
        
    def withdraw(self):
        print("You withdrew all the money in your account.\n")
    def balance(self):
        print("You have $0 in your account.\n")
    def deposit(self):
        print("You deposited some money in your account.\n")

account1 = Atm("1234 5678 9101 2131","123456","0")
card = input("What is your card number?\n")
if(card == account1.cardNo):
    pin = input("\nWhat is your pin number?\n")
    if(pin == account1.pinNo):
        what = input("\nWhat would you like to do?\n")
        if(what == "Withdraw"):
            account1.withdraw()
            print("Thank you for using our service.\n")
        elif(what == "Balance"):
            account1.balance()
            print("Thank you for using our service.\n")
        elif(what == "Deposit"):
            account1.deposit()
            print("Thank you for using our service.\n")
        else:
            print("Sorry, that is an invalid action.")
    else:
        print("You have typed the incorrect pin. This session has ended. Thank you for using our service.\n")
else:
    print("No such account exists.")
    
