class Plant:
    """
    A class used to represent a Plant in the garden.

    Attributes:
        name (str): The name of the plant (e.g., 'Rose').
        height (int): The current height of the plant in cm.
        plant_age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        """
        Initializes a new Plant object with name, height, and age.

        Args:
            name (str): The name of the plant.
            height (int): The initial height in centimeters.
            plant_age (int): The initial age in days.
        """
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self, cm: int = 1) -> None:
        """
        Increases the height of the plant.

        Args:
            cm (int, optional): The amount to grow in cm. Defaults to 1.
        """
        self.height += cm

    def age(self, days: int) -> None:
        """
        Increases the age of the plant.

        Args:
            days (int, optional): The number of days to age. Defaults to 1.
        """
        self.plant_age += days

    def get_info(self) -> None:
        """
        Generates a formatted string containing the plant's current status.

        Returns:
            str: A string describing the name, height, and age.
        """
        print(f"Created: {self.name} ({self.height}cm, {self.plant_age} days)")


# set up plants
plat_data = [
    ("Rose", 25, 30),
    ("Sunflower", 80, 45),
    ("Cactus", 5, 90),
    ("Oak", 200, 365),
    ("Fern", 15, 120)
    ]

if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    i = 0
    for plant in plat_data:
        new_plant = Plant(*plant)
        new_plant.get_info()
        i += 1

    print(f"Total plants created: {i}")
