from abc import ABC, abstractmethod

class Startup(ABC):
    @abstractmethod
    def build(self):
        pass

    def fund(self):
        print("boostrapping...")

class Swiggy(Startup):
    
    def build(self):
        print("food delivery service")
    
class Uber(Startup):
    
    def build(self):
        print("ride at as service")
    
class Amazon(Startup):

    def build(self):
        print("online shopping")
    
    def fund(self):
        print("Series A...")

def main():
    
# uncomment and check , it will throw an error as 
# Can't instantiate abstract class Startup with abstract methods build

    # startup = Startup()
    # startup.build()
    # startup.fund()
    
    s = Swiggy()
    s.build()
    s.fund()

    a = Amazon()
    a.build()
    a.fund()

    u = Uber()
    u.build()
    u.fund()

if __name__ == "__main__":
    main()


