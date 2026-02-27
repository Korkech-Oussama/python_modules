def test_validation() -> None:
    from alchemy.grimoire.validator import validate_ingredients
    print(f"validate_ingredients(\"fire air\"):" +
          f"{validate_ingredients("fire air")}")
    print(f"validate_ingredients(\"dragon scales\"):" +
          f"{validate_ingredients("dragon scales")}")


def test_spell() -> None:
    print("Testing spell recording with validation:")


if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")
    test_validation()