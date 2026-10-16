class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        # This creates a new private attribute for account_number
        self.set_balance(balance)
        # We use this setter for balance to initialize balance attribute while checking it isnt negative.

 
    def set_account_number(self, account_number): # We create a setter method here to update the balance. 
        self.__account_number = account_number 

    
    def set_balance(self, balance): # This defines a public setter method to check if balance is negative.
        if balance < 0: # This checks if the balance provided is negative.
            print("The balance must be not be a negative number.") # This prints if it is negative
        else: 
            self.__balance = float(balance) # If balance is not negative it converts balance into a float and stores it within self.__balance attribute. 
       
   # This is a getter for account_number attribute
    @property # I put this here so that account_number despite being a method can be accessed as a attribute.
    def account_number(self): # This defines the getter method.
        return self.__account_number # This returns the value when account_number is used.

    @property # It is the same as the first instance of @property, I use it so balance is treated as a attribute.
    def balance(self):
        return self.__balance # This returns the self.__balance attribute when requested.


# Example usage for Bank Account class 
print("Object of class BankAccount\n") # This is an example scenario using the bankaccount class.
a1 = BankAccount(12345, 1000) # This creates the object.

print("Output:") # Both this(line 33 and 34) is just to make output look better.
print("Account 1") 
print(f"Account Number: {a1.account_number}") # This prints the first attribute(account_number)
print(f"Balance: {a1.balance:.2f}\n") # This prints balance but formatted into having 2 decimal places.

print("Update balance to -100") # This follows sample output and tests what happens if money from balance is withdrawn.
a1.set_balance(-100) # We use set_balance to update its value by -100
print(f"Account Number: {a1.account_number}") # This prints the after result
print(f"Balance: {a1.balance:.2f}") # The final balance.
