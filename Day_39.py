class user():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender 
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

class Bank():
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account Balance has been updated: Rs.", self.balance)
    def withdraw(self,amount):
        self.amount = amount
        if self.amount>self.balance:
            print("Insufficient Fund || Balance Available : Rs.",self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account Balance had been updated : Rs.",self.balance)
        def view(self):
            self.show_details()
            print("Account Balance had been updated : Rs.",self.balance)
            