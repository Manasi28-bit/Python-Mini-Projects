import datetime

class ATM:
    def __init__(self, name):
        self.name = name.title()
        self.__balance = 0
        self.sr = 0
        self.__create_pin()
        self.__create_passbook()

    def deposit(self, amt):
        if self.__check_pin():
            if amt > 0:
                self.__balance += amt
                print(f"₹{amt} credited successfully.")
                self.__log("Credited", amt)
            else:
                print("Invalid amount.")

    def withdraw(self, amt):
        if self.__check_pin():
            if amt <= 0:
                print("Invalid amount.")
            elif amt % 100 != 0:
                print("Amount must be multiple of 100.")
            elif amt > self.__balance:
                print("Insufficient balance.")
            else:
                self.__balance -= amt
                print(f"₹{amt} debited successfully.")
                self.__log("Debited", amt)

    def check_balance(self):
        if self.__check_pin():
            print(f"Current balance: ₹{self.__balance}")

    def __create_pin(self):
        while True:
            pin = input("Create 4-digit PIN: ")
            confirm = input("Re-enter PIN: ")
            if pin.isdigit() and len(pin) == 4 and pin == confirm:
                self.__pin = pin
                print("PIN created successfully.")
                break
            else:
                print("Invalid PIN. Try again.")

    def __check_pin(self):
        attempts = 3
        while attempts > 0:
            pin = input("Enter PIN: ")
            if pin == self.__pin:
                return True
            attempts -= 1
            print(f"Wrong PIN. {attempts} attempt(s) left.")
        print("Card blocked.")
        return False

    def __create_passbook(self):
        with open(self.name + ".txt", "w") as f:
            f.write(f"Account Holder: {self.name}\n")
            f.write("Sr  Date & Time                Status     Amount   Balance\n")

    def __log(self, status, amt):
        self.sr += 1
        with open(self.name + ".txt", "a") as f:
            f.write(f"{self.sr}  {datetime.datetime.now()}  {status}  ₹{amt}  ₹{self.__balance}\n")

    def print_passbook(self):
        if self.__check_pin():
            with open(self.name + ".txt", "r") as f:
                print(f.read())
