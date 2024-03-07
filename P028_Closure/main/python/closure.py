'''
Created on Mar 7, 2024

@author: witek
'''
def create_account(initial_balance=0):
    balance = initial_balance
        
    def deposit(amount):
        nonlocal balance
        balance += amount
        return f"Deposited {amount}. New balance: {balance}"
    
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return f"Withdrawn {amount}. New balance: {balance}"
        else:
            return "Insufficient funds."
        
    def check_balance():
        return f"Current balance: {balance}"
    
    return deposit, withdraw, check_balance

account_deposit, account_withdraw, account_balance = create_account(1000)
deposit, withdraw, balance = create_account(324)
zero_deposit, zero_withdraw, zero_balance = create_account()

print(account_balance())
print(account_deposit(500))
print(account_withdraw(200))
print(balance())
print(deposit(500))
print(withdraw(200))
print(zero_balance())
print(zero_deposit(500))
print(zero_withdraw(200))
print(zero_balance())
print(zero_withdraw(1500))
print(balance())
print(withdraw(1500))
print(account_balance())
print(account_withdraw(1500))