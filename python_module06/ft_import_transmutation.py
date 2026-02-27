def diff_import_styles() -> None:
    print("Method 1 - Full module import:")
    try:
        import alchemy.elements
        print("alchemy.elements.create_fire(): "
              f"{alchemy.elements.create_fire()}\n")
    except Exception as e:
        print(e)


def specific_import() -> None:
    print("Method 2 - Specific function import:")
    try:
        from alchemy.elements import create_water
        print(f"create_water(): {create_water()}\n")
    except Exception as e:
        print(e)


def aliased_imports() -> None:
    print("Method 3 - Aliased import:")
    try:
        from alchemy.potions import healing_potion as heal
        print(f"heal(): {heal()}\n")
    except Exception as e:
        print(e)


def multiple_imports() -> None:
    print("Method 4 - Multiple imports:")
    try:
        from alchemy.elements import create_earth, create_fire
        from alchemy.potions import strength_potion
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strength_potion()}\n")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===\n")
    diff_import_styles()
    specific_import()
    aliased_imports()
    multiple_imports()

    print("All import transmutation methods mastered!")
