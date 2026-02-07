class Plant:
    """
    A base class used to represent a generic Plant.

    Attributes:
        name (str): The name of the plant.
        height (int): The height in cm.
        age (int): The age in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the base plant attributes."""
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        classname = self.__class__.__name__
        """Returns a formatted string representing the plant's basic info."""
        return f"{self.name} ({classname}): {self.height}cm, {self.age} days"


class Flower(Plant):
    """
    Represents a Flower, inheriting from Plant.

    Attributes:
        color (str): The color of the flower petals.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes flower and calls parent setup."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Prints a message about the flower blooming."""
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        """Extends parent string with color info."""
        return f"{super().__str__()}, {self.color} color"


class Tree(Plant):
    """
    Represents a Tree, inheriting from Plant.

    Attributes:
        trunk_diameter (int): The diameter of the tree trunk in cm.
    """

    def __init__(self, name: str, height: int,
                 age: int, diameter: int) -> None:
        """Initializes tree and calls parent setup."""
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def produce_shade(self, shade_area: int) -> None:
        """Prints the amount of shade provided."""
        print(f"{self.name} provides {shade_area} square meters of shade")

    def __str__(self) -> str:
        """Extends parent string with diameter info."""
        return f"{super().__str__()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """
    Represents a Vegetable, inheriting from Plant.

    Attributes:
        harvest_season (str): The season when it is harvested.
        nutritional_value (str): The main vitamin or nutrient content.
    """

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initializes vegetable and calls parent setup."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def vegetable_info(self) -> None:
        """Prints the nutritional benefits of the vegetable."""
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

    def __str__(self) -> str:
        """Extends parent string with season info."""
        return f"{super().__str__()}, {self.harvest_season} harvest"


def main():
    print("=== Garden Plant Types ===")

    # Creating 2 instances of Flower
    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 15, 12, "white")

    print(rose)
    rose.bloom()
    print(lily)
    lily.bloom()

    # Creating 2 instances of Tree
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 1000, 30)

    print(oak)
    oak.produce_shade(78)
    print(pine)
    pine.produce_shade(40)

    # Creating 2 instances of Vegetable
    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    carrot = Vegetable("Carrot", 20, 70, "autumn", "A")

    print(tomato)
    tomato.vegetable_info()
    print(carrot)
    carrot.vegetable_info()


if __name__ == "__main__":
    main()
