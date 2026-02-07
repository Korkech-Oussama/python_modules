class Plant:
    """
    A base class used to represent a generic Plant.

    Attributes:
        name (str): The name of the plant.
        height (int): The height in cm.
    """

    def __init__(self, name: str, height: int) -> None:
        """
        Initializes the base plant attributes.

        Args:
            name (str): The name of the plant.
            height (int): The starting height in cm.
        """
        self.name = name
        self.height = height

    def grow(self, cm: int) -> None:
        """
        Increases the plant's height and logs the growth.

        Args:
            cm (int): The amount of growth in centimeters.
        """
        self.height += cm
        print(f"{self.name} grew {cm}cm")

    def __str__(self) -> str:
        """
        Returns a formatted string representing the plant's basic info.

        Returns:
            str: The formatted string (e.g., 'Oak: 100cm').
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Represents a plant that produces flowers.
    Inherits from Plant.
    """

    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initializes a flowering plant with a specific color.

        Args:
            name (str): The name of the plant.
            height (int): The starting height in cm.
            color (str): The color of the flowers.
        """
        super().__init__(name, height)
        self.color = color

    def __str__(self) -> str:
        """
        Adds flowering details to the string representation.
        """
        return f"{super().__str__()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """
    Represents a special flower entered in a competition.
    Inherits from FloweringPlant.
    """

    def __init__(self, name: str, height: int, color: str, score: int) -> None:
        """
        Initializes a prize flower with competition points.

        Args:
            name (str): The name of the plant.
            height (int): The starting height in cm.
            color (str): The color of the flowers.
            score (int): The prize points assigned to this flower.
        """
        super().__init__(name, height, color)
        self.score = score

    def __str__(self) -> str:
        """
        Adds prize points to the string representation.
        """
        return f"{super().__str__()}, Prize points : {self.score}"


class GardenManager:
    """
    Manages a garden, tracks plants, and calculates statistics.

    Attributes:
        total_gardens (int): Class attribute tracking total managers created.
    """
    total_gardens: int = 0

    class GardenStats:
        """Nested helper class for statistical analysis."""

        @staticmethod
        def analyze(plants: list) -> tuple[int, int, int, int, int]:
            """
            Analyzes the plant list to return counts and scores.

            Args:
                plants (list): A list of Plant objects.

            Returns:
                tuple: (count, regular, flowering, prize, total_score)
            """
            count: int = 0
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            score: int = 0

            for plant in plants:
                count += 1
                score += plant.height

                if isinstance(plant, FloweringPlant):
                    score += 15
                    if type(plant) is FloweringPlant:
                        flowering += 1

                if isinstance(plant, PrizeFlower):
                    score += plant.score
                    prize += 1

                if type(plant) is Plant:
                    regular += 1

            return (count, regular, flowering, prize, score)

    def __init__(self, manager: str) -> None:
        """
        Initializes a new GardenManager.

        Args:
            manager (str): The name of the garden owner.
        """
        self.manager = manager
        self.plants: list = []
        self.growth: int = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """
        Adds a plant to the garden inventory.

        Args:
            plant (Plant): The plant object to add.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.manager}'s garden")

    def grow_all(self, cm: int) -> None:
        """
        Triggers growth for all plants in the garden.

        Args:
            cm (int): The growth amount in centimeters.
        """
        print(f"\n{self.manager} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)
            self.growth += cm

    @staticmethod
    def valid_height(height: int) -> bool:
        """
        Utility to validate if a height is positive.

        Args:
            height (int): The height to check.

        Returns:
            bool: True if valid, False otherwise.
        """
        return height > 0

    @classmethod
    def create_garden_manager(cls, *managers: str) -> list:
        """
        Factory method to create multiple GardenManager instances.

        Args:
            *managers (str): Variable number of owner names.

        Returns:
            list: A list of new GardenManager objects.
        """
        managers_list = []
        for manager in managers:
            new_manager = cls(manager)
            managers_list.append(new_manager)
        return managers_list

    def display_report(self) -> None:
        """
        Prints a detailed report of the current garden state.
        """
        print(f"\n=== {self.manager}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")

        count, reg, flow, prize, score = self.GardenStats.analyze(self.plants)

        print(f"\nPlants added: {count}, Total growth: {self.growth}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prize} prize flowers")
        print(f"Height validation test: {self.valid_height(score)}")


plant1 = Plant("Oak Tree", 100)
plant2 = FloweringPlant("Rose", 25, "red")
plant3 = PrizeFlower("Sunflower", 50, "yellow", 10)
plant4 = PrizeFlower("Jasmin", 60, "purple", 20)

garden = [plant1, plant2, plant3]

if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # Create Managers
    alice, bob = GardenManager.create_garden_manager("Alice", "Bob")

    # Alice's Operations
    for plant in garden:
        alice.add_plant(plant)

    alice.grow_all(1)
    alice.display_report()

    # Bob's Operations
    bob.add_plant(plant4)
    bob.display_report()

    # Final Summary
    alice_score = alice.GardenStats.analyze(alice.plants)[4]
    bob_score = bob.GardenStats.analyze(bob.plants)[4]

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
