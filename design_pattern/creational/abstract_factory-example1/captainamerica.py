from character import Character

class CaptainAmerica(Character):

    def __init__(self,name):
        Character.__init__(self)
        self.type = 'CaptainAmerica'
        self.__name = name
        self.__power = 'strategy'

    def set_new_special_power(self,power):
        self.__power = power
    
    def set_hit_points(self):
        points = random.randint(4,8)
        self.__hit_points=points

    def set_health_points(self):
        points = random.randint(35,66)
        self.__health_points=points

    def get_info(self):
        print("--------- INFO ---------") 
        print(f"Hero: {self.type}")
        print(f"Special power: {self.__power}")
        print(f"Hit points: {self.__hit_points}")
        print(f"Health points: {self.__health_points}")

    def get_power_bonus(self):
        power = self.power_bonus.get(self.__power)
        return power
    


