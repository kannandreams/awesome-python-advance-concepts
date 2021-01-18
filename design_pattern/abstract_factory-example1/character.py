from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self):
        self.__hit_points=None
        self.__health_points=None

    @abstractmethod
    def set_hit_points(self):
        pass

    @abstractmethod
    def set_health_points(self):
        pass

    @abstractmethod
    def get_info(self):
        pass 