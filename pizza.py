import math


class Pizza:
    __price: float
    __toppings: dict[str, int]
    __diameter: float

    def __init__(self, diameter: float = 0, toppings: dict[str, int] = None) -> None:
        self.__diameter = diameter
        self.__toppings = toppings

    @staticmethod
    def area(diameter) -> float:
        if diameter < 20:
            print("Bledna srednica")
        else:
            return math.pi * pow((diameter / 2), 2)

    # price = 0.05 * area

    @property
    def diameter(self) -> float:
        return self.__diameter

    @diameter.setter
    def diameter(self, value: float) -> None:
        if value > 20:
            self.__diameter = value
        else:
            print("Bledna srednica")

    # def add_topping(self) -> str:

    def __str__(self) -> str:
        if self.__toppings == 0:
            return f"srednica: {self.__diameter} \n" \
                   f"dodatki: {self.__toppings} \n" \
                   f"cena: {self.__price}"
        else:
            return f"srednica: {self.__diameter} \n" \
                   f"cena: {self.__price}"
