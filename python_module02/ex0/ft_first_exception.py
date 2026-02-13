def check_temperature(temp_str: str) -> int:
    print(f"Testing temperature: {temp_str}")
    try:
        temp_num = int(temp_str)
        if temp_num > 40:
            print(f"Error: {temp_num}°C is too hot for plants (max 40°C)\n")
        elif temp_num < 0:
            print(f"Error: {temp_num}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {temp_num}°C is perfect for plants!\n")
            return temp_num
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
