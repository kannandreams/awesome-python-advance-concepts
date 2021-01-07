'Polymorphism example'

class Account():
    'This is base class'
    def __init__(self,holder):
        self.holder = holder

    def __str__(self):
        return self.holder + " like to open account in our bank"
    
class Savings(Account):
    
    # def __init__(self,holder,deposit):
    #     self.holder=holder
    #     self.deposit = deposit

    'Instead of defining everything in sub class constructor,we can invoke the base class constructor'
    def __init__(self,holder,deposit):
        super().__init__(holder)
        self.deposit = deposit


    # def __str__(self):
    #     return self.holder + " like to open account in our bank with deposit of " + str(self.deposit)

    def __str__(self):
        return super().__str__() + " with deposit of " + str(self.deposit)

def main():
    account = Account("Avenger")
    print(account)

    account = Savings("Avenger",1000)
    print(account)

if __name__ == "__main__":
    print(__doc__)
    main()
