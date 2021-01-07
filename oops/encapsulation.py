class Account():
    def __init__(self):
        """ Access modifiers example """
        self.bank = "Citi Bank" # public 
        self._owner = "US" # private because of underscore before the variable
        self.__secretcode = "000" # strictly private with double underscore

def main():
    a = Account()
    print(a.bank)
    print(a._owner)
    #uncomment to check . it will throw Error: 'Account' object has no attribute '__secretcode'
    #print(a.__secretcode)  

    # in order to access strictly underscore variable by following like this.
    print(a._Account__secretcode) 

if __name__ == "__main__":
    main()