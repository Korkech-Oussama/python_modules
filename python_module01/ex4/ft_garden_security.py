class SecurePlant:
    """
    A class representing a plant with encapsulated data to prevent corruption.

    This class protects sensitive attributes like height and age by making them
    protected (using _) and requiring access through validated setter methods.

    Attributes:
        name (str): The public name of the plant.
        _height (int): The protected height in cm.
        _plant_age (int): The protected age in days.
    """

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        """
        Initializes a new SecurePlant object.

        Note:
            We use the setters immediately here to ensure validation rules
            apply even during creation (e.g., rejecting negative start values).

        Args:
            name (str): The name of the plant.
            height (int): The initial height in centimeters.
            plant_age (int): The initial age in days.
        """
        self.name = name
        # We initialize with unsafe values first, then validate them properly
        self._height = 0
        self._plant_age = 0

        # Use the secure setters to apply validation immediately
        self.set_height(height)
        self.set_age(plant_age)

    def set_height(self, height: int) -> None:
        """
        Safely updates the plant's height after validation.

        Checks if the height is a non-negative integer. If invalid,
        the update is rejected and an error is logged.

        Args:
            height (int): The new height in centimeters.
        """
        if not type(height) is int or height < 0:
            print(f"\nInvalid operation attempted: height {height}"
                  + "cm [REJECTED]")
            print("Security: Negative or invalid height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Safely updates the plant's age after validation.

        Checks if the age is a non-negative integer. If invalid,
        the update is rejected and an error is logged.

        Args:
            age (int): The new age in days.
        """
        if not type(age) is int or age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative or invalid age rejected")
        else:
            self._plant_age = age
            print(f"Age updated: {self._plant_age} days [OK]")

    def get_height(self) -> int:
        """
        Retrieves the current height of the plant.

        Returns:
            int: The height in centimeters.
        """
        return self._height

    def get_age(self) -> int:
        """
        Retrieves the current age of the plant.

        Returns:
            int: The age in days.
        """
        return self._plant_age

    def display_name_plant(self) -> None:
        """
        Prints a confirmation message with the plant's name.
        """
        print(f"Plant created: {self.name}")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 10, 58)
    plant.display_name_plant()
    plant.set_age(11)
    plant.set_height(-2)

    name = plant.name
    age = plant.get_age()
    height = plant.get_height()
    print(f"\nCurrent plant: {name} ({height}cm, {age})")
