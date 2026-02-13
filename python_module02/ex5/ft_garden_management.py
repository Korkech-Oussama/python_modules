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

class GardenManager:
    def __init__(self, name: str, water_level:int, sunlight_hours: int):
        self.plant_name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.plants = []

    def add_plant(self, plant: tuple) -> None:
        print("Adding plants to garden...")
        try:
            if self.plant_name == "":
                raise PlantError("Plant name cannot be empty!\n")
            elif self.water_level > 10:
                raise GardenError(f"Water level {self.water_level} is too high (max 10)\n")
            elif self.sunlight_hours < 2:
                raise GardenError(f" Sunlight hours {self.sunlight_hours} is too low (min 2)\n")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            self.plants.append(plant)
            print(f"Added {self.plant_name} successfully")

    def  check_plant_health(self) -> None:
        try:
            if self.plant_name == "":
                raise GardenError(" Plant name cannot be empty!\n")
            elif self.water_level > 10:
                raise GardenError(f"Water level {self.water_level} is too high (max 10)\n")
            elif self.sunlight_hours < 2:
                raise GardenError(f" Sunlight hours {self.sunlight_hours} is too low (min 2)\n")
        except GardenError as e:
            print(f"Error checking {self.plant_name}: {e}")
        else:
            print(f"{self.plant_name}: healthy!(water: {self.water_level}, sun: {self.sunlight_hours})")


    def water_plants(self) -> None:
        print("Watering plants")
        try:
            for plant in self.plants:
                if plant.name is None:
                    raise GardenError(f"Cannot water {plant.name} - invalid plant!")
                else:
                    print(f"Watering {plant} - success")
        except GardenError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    @staticmethod
    def water_quantity(liters: int):
        try:
            if liters < 0:
                raise GardenError("Not enough water in the tank!")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...")



    