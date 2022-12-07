from pizza import Pizza


class Slice(Pizza):
    __how_many_slices: int

    def __init__(self, price: float, diameter: float, toppings: dict, how_many_slices: int) -> None:
        super().__init__(price, toppings, diameter)
        self.__how_many_slices = how_many_slices

    @property
    def how_many_slices(self) -> int:
        return self.__how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, value: int) -> None:
        if 4 <= value <= 12 and value % 2 == 0:
            self.__how_many_slices = value
        else:
            print("Bledna ilosc kawalkow")

    @how_many_slices.getter
    def how_many_slices(self) -> int:
        return self.__how_many_slices

    def __str__(self) -> str:
        if self.__toppings == 0:
            return f"srednica: {self.__diameter} \n" \
                   f"cena: {self.__price} \n" \
                   f"kawalki: {self.__how_many_slices} \n" \
                   f"cena za kawalek: "
        else:
            return f"srednica: {self.__diameter} \n" \
                   f"dodatki: {self.__toppings} \n" \
                   f"cena: {self.__price}"
