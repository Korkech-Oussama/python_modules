def  check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    try:
        if plant_name == "":
            raise ValueError(" Plant name cannot be empty!\n")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)\n")
        elif sunlight_hours < 2:
            raise ValueError(f" Sunlight hours {sunlight_hours} is too low (min 2)\n")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Plant 'tomato' is healthy!\n")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    values: tuple = ("tomato", 9, 3)
    print("Testing good values...")
    check_plant_health(*values)

    values: tuple = ("", 9, 3)
    print("Testing empty plant name...")
    check_plant_health(*values)

    values: tuple = ("tomato", 15, 3)
    print("Testing bad water level...")
    check_plant_health(*values)

    values: tuple = ("tomato", 9, 1)
    print("Testing bad sunlight hours...")
    check_plant_health(*values)

    print("All error raising tests completed!")

if __name__ == "__main__":
    test_plant_checks()