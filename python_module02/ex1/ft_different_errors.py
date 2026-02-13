def garden_operations(error_type: str) -> None:
    plants: dict = {"oak": "tree"}
    if error_type == "ValueError":
        int("abc")
    if error_type == "ZeroDivisionError":
        1 / 0
    if error_type == "FileNotFoundError":
        open("!existing.txt")
    if error_type == "KeyError":
        plants["flower"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing Keyrror...")
    try:
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("ZeroDivisionError")
    except (ValueError, KeyError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
