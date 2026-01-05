class account:
    bankIFSCcode="SBI103872656"
    def __init__(self,name,no,balance):
        self.name=name
        self.accountno=no
        self.balance=balance
    def deposit(self,amountd):
        self.balance+=amountd
        print(f"Amount of rupees {amountd}.00 deposited into your account successfully.Your current account balance is {self.balance}.00.")
    def withdraw(self,amountw):
        if self.balance<amountw:
            print("Sorry,Your check is bounced.")
        else:    
            self.balance-=amountw 
            print(f"Amount of rupees {amountw}.00 withdrawn from your account successfully.Your current account balance is {self.balance}.00.")
    def showaccountdetails(self):
        print(f"""Your account details are as follows :
              Bank's IFSC code={account.bankIFSCcode}
              Your name={self.name}
              Your account no.={self.accountno}
              Your account balance={self.balance}""") 
People=[]   
i=0          
while i>=0:
    command=input("Enter the command:")
    if command=="Exit":
        break 
    else:
        if command=="Create a new account:":
            i+=1
            name=input("Lets create your account first.Enter your name:")
            import random 
            accountno=random.randrange(10000000000,1000000000000)
            balance=0 
            person=account(name,accountno,balance)
            People.append(person)
            print("Account created successfully.")
        elif command=="Deposit the given amount:":
            amount=int(input("Enter the amount you wanna deposit:"))
            person.deposit(amount)
        elif command=="Withdraw the given amount:":
            amount=int(input("Enter the amount you wanna withdraw from your account:"))
            person.withdraw(amount)
        elif command=="Show my account details.":
            person.showaccountdetails()
        else :
            print("Command is not valid.") 



                   
