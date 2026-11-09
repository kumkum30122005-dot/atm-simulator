class Atm:

  def __init__(self):
    self.balance = 0
    self.pin = ''
    self.menu()

  def menu(self):

    while(true):
    user_input = input("""
        Hi how can I help you ??
        1: press 1 for creating the pin.
        2: press 2 for changing the pin.
        3: press 3 for checking the balance.
        4: press 4 to withdraw money.
        5: Anything else to exit.
    """)

    if user_input == '1':
      self.create_pin()
      self.menu()

    elif user_input == '2':
      self.change_pin()
      self.menu()
    
    elif user_input == '3':
      self.check_balance()
      self.menu()

    elif user_input == '4':
      self.withdraw_money()
      self.menu()

    else: 
      print("Exiting... Thanks for using!")


  def create_pin(self):
    user_pin = int(input("enter the pin: "))
    user_balance = int(input("enter the balance: "))
    self.pin = user_pin
    self.balance = user_balance
    print("pin successfully created.")

  def change_pin(self):
    old_pin = int(input("enter your old pin: "))
    if old_pin == self.pin:
      new_pin = int(input("enter the new pin: "))
      self.pin = new_pin
      print("pin successfully updated.")
    else:
      print("Wrong pin")

  def check_balance(self):
    user_pin = int(input("enter the pin: "))
    if user_pin == self.pin:
      print("Your current balance is: ", self.balance)
    else:
      print("Invalid pin.")

  def withdraw_money(self):
    user_pin = int(input("enter the pin: "))
    if user_pin == self.pin:
      amount_withdraw = int(input("enter the amount to withdraw: "))
      if amount_withdraw <= self.balance:
        self.balance = self.balance - amount_withdraw
        print("The current balance is", self.balance)
      else:
        print("balance Insufficient.")
    else:
      print("Invalid pin")

obj = Atm()
