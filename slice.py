from pizza import Pizza


class Slice(Pizza):
    __how_many_slices: int

    def __init__(self, diameter: float = 0, toppings: dict[str, int] = None, how_many_slices: int = 0) -> None:
        super().__init__(toppings, diameter)
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

    def part_price(self, ordered_slices, __how_many_slices, price) -> int:
        __ordered_slices = __price*(__/__how_many_slices


    def __str__(self) -> str:
        if self.__toppings == 0:
            return f"srednica: {self.__diameter} \n" \
                   f"cena: {self.__price} \n" \
                   f"kawalki: {self.__how_many_slices} \n" \
                   f"cena za kawalek: {self.__price/self.__how_many_slices}"
        else:
            return f"srednica: {self.__diameter} \n" \
                   f"dodatki: {self.__toppings} \n" \
                   f"cena: {self.__price} \n" \
                   f"kawalki: {self.__how_many_slices} \n" \
                   f"cena za kawalek: {self.__price/self.__how_many_slices}"