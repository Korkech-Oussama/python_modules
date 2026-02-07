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


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
lst = [plant1, plant2, plant3]


def print_plant_infos():
    print("=== Garden Plant Registry ===")
    for p in range(0, 3):
        print(f"{lst[p].name}: {lst[p].height}cm, {lst[p].plant_age} days old")


if __name__ == "__main__":
    print_plant_infos()
