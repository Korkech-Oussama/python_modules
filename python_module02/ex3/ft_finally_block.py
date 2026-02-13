def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    plant_list: list = ["tomato", "lettuce", "carrots"]
    plant_lst: list = ["tomato", None]
    print("Testing normal watering...")
    water_plants(plant_list)

    print("Testing with error...")
    water_plants(plant_lst)

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
