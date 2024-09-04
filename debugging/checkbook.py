#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        """
        Initialize a new Checkbook instance with a starting balance of $0.00.
        
        Function Description:
        This constructor method sets up the initial balance of the checkbook.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.
        
        Function Description:
        This method adds the provided amount to the current balance and prints
        the updated balance.
        
        Parameters:
        amount (float): The amount of money to deposit. Must be a non-negative number.
        
        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook if sufficient funds are available.
        
        Function Description:
        This method subtracts the provided amount from the current balance if there
        are enough funds available. It prints an error message if the withdrawal cannot
        be completed due to insufficient funds.
        
        Parameters:
        amount (float): The amount of money to withdraw. Must be a non-negative number.
        
        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.
        
        Function Description:
        This method prints the current balance of the checkbook.
        
        Parameters:
        None
        
        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class.
    
    Function Description:
    This function provides a command-line interface to interact with the Checkbook
    class. Users can deposit, withdraw, check the balance, or exit the program.
    
    Parameters:
    None
    
    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        
        if action == 'exit':
            print("Exiting the program.")
            break
        
        if action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif action == 'balance':
            cb.get_balance()
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
