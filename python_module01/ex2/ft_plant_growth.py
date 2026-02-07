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
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


# set up plants
plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
garden = [plant1, plant2, plant3]


if __name__ == "__main__":
    print("=== Day 1 ===")
    start_height = plant1.height

    # Display initial state
    for plant in garden:
        plant.get_info()

    # Simulate 6 days of growth
    for day in range(6):
        for plant in garden:
            plant.age(1)
            plant.grow(1)

    print("=== Day 7 ===")
    for plant in garden:
        plant.get_info()

    final_height = plant1.height
    print(f"Growth this week : +{final_height - start_height}cm")
