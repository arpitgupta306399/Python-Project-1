class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print("Amount Deposited Successfully!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            print("Amount Withdrawn Successfully!")
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")
    def show_transactions(self):
        print("\nTransaction History:")
        for t in self.transactions:
            print(t)
print("====== Welcome to Simple Bank System ======")
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))
account = BankAccount(name, balance)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        account.show_transactions()
    elif choice == "5":
        print("Thank You for Using Bank System!")
        break
    else:
        print("Invalid Choice! Try Again.")

