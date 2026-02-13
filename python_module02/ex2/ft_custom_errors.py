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


def soil_status(status: str):
    if status == "bad":
        raise PlantError("The tomato plant is wilting!")


def water_quantity(liters: int):
    if liters < 0:
        raise WaterError("Not enough water in the tank!")


def check_garden():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        soil_status("bad")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        water_quantity(-5)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        soil_status("bad")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_quantity(-10)
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    check_garden()
