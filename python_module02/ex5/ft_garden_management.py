class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.plant_name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self):
        self.plants = []

    @staticmethod
    def validate_plant_data(plant: Plant):
        if plant.plant_name == "":
            raise PlantError("Plant name cannot be empty!\n")
        elif plant.water_level > 10:
            raise GardenError(f"Water level {plant.water_level} " +
                              "is too high (max 10)\n")
        elif plant.sunlight_hours < 2:
            raise GardenError(f" Sunlight hours {plant.sunlight_hours} " +
                              "is too low (min 2)\n")

    def add_plant(self, plant: Plant) -> None:
        try:
            self.validate_plant_data(plant)
        except GardenError as e:
            print(f"Error adding plant: {e}")
        else:
            self.plants.append(plant)
            print(f"Added {plant.plant_name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                print("No plants to water.")
                return
            for plant in self.plants:
                print(f"Watering {plant.plant_name} - success")
        except GardenError as e:
            print(f"Error during watering: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self, plant: Plant) -> None:
        try:
            self.validate_plant_data(plant)
        except GardenError as e:
            print(f"Error checking {plant.plant_name}: {e}")
        else:
            print(f"{plant.plant_name}: healthy!" +
                  "(water: {plant.water_level}, sun: {plant.sunlight_hours})")

    @staticmethod
    def water_quantity(liters: int):
        try:
            if liters < 0:
                raise GardenError("Not enough water in the tank!")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...\n")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    plant_data = [
        Plant("tomato", 5, 8),
        Plant("lettuce", 3, 3),
        Plant("", 5, 7)
    ]
    manager = GardenManager()

    print("Adding plants to garden...")
    for plant in plant_data:
        manager.add_plant(plant)

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant health...")
    for plant in manager.plants:
        manager.check_plant_health(plant)

    print("\nTesting error recovery...")
    manager.water_quantity(-1)

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
