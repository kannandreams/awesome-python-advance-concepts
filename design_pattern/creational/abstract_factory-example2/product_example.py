from __future__ import annotations
from abc import ABC, abstractmethod


class HouseFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def build_wall(self) -> AbstractWall:
        pass

    @abstractmethod
    def paint_wall(self) -> AbstractPaint:
        pass


class LowBudgetHouse(HouseFactory):
    def build_wall(self) -> AbstractWall:
        return ConcreteFireBrick()

    def paint_wall(self) -> AbstractPaint:
        return ConcreteEmulsion()


class EcoFriendlyHouse(HouseFactory):
    def build_wall(self) -> AbstractWall:
        return ConcreteCinderBrick()

    def paint_wall(self) -> AbstractPaint:
        return ConcreteMilkPaint()


class AbstractWall(ABC):
    @abstractmethod
    def build(self) -> str:
        pass

class ConcreteFireBrick(AbstractWall):
    def build(self) -> str:
        return "The wall is build by FireBrick"


class ConcreteCinderBrick(AbstractWall):
    def build(self) -> str:
        return "The wall is build by CinderBrick"


class AbstractPaint(ABC):
    @abstractmethod
    def select_paint(self) -> None:
        pass

    @abstractmethod
    def brush(self, collaborator: AbstractWall) -> None:
        pass

class ConcreteEmulsion(AbstractPaint):
    def select_paint(self) -> str:
        return "Selected paint is Emulsion"

    def brush(self, collaborator: AbstractWall) -> str:
        result = collaborator.build()
        return f"{result} and {self.select_paint()}"


class ConcreteMilkPaint(AbstractPaint):
    def select_paint(self) -> str:
        return "Selected paint is Milk Paint"

    def brush(self, collaborator: AbstractWall) -> str:
        result = collaborator.build()
        return f"{result} and {self.select_paint()}"


def client_code(factory: HouseFactory) -> None:

    wall = factory.build_wall()
    paint = factory.paint_wall()

    print(f"{wall.build()}")
    print(f"{paint.brush(wall)}")


if __name__ == "__main__":
    print("Client: design a low budget house for me")
    client_code(LowBudgetHouse())

    print("\n")

    print("Client: design a eco friendly  house for me")
    client_code(EcoFriendlyHouse())