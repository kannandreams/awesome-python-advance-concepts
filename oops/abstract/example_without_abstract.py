class Startup:

    def build(self):
        print("Build Startup")

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
    
    startup = Startup()
    startup.build()
    startup.fund()
    
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

""" 
In real world, we can't build startup at abstract level and there is no meaning. 
 it should be specific startup at any point like swiggy, uber, amazon,etc. 
  Abstract is concept level.
"""
