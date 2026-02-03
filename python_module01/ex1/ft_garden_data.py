#!/usr/bin/env python3
class Plant:
    """
    docstring needed
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)


def print_plant_infos():
    print("=== Garden Plant Registry ===")
    print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")


if __name__ == "__main__":
    print_plant_infos()
