#!/usr/bin/env python3
name = "Rose"
height = 25
age = 30


def print_garden_info():
    """
        this function prints the 3 following Variables
        name (str): The name of the plant.
        height (int): The initial height in centimeters.
        plant_age (int): The initial age in days.
    """
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    print_garden_info()
