def test_validation() -> None:
    try:
        print("Testing ingredient validation:")
        from alchemy.grimoire.validator import validate_ingredients
        print("validate_ingredients(\"fire air\"):" +
              f"{validate_ingredients("fire air")}")
        print("validate_ingredients(\"dragon scales\"):" +
              f"{validate_ingredients("dragon scales")}")
    except Exception as e:
        print(e)


def test_spell() -> None:
    try:

        from alchemy.grimoire.spellbook import record_spell
        print("\nTesting spell recording with validation:")
        print("record_spell(\"Fireball\", \"fire air\"): " +
              f"{record_spell("Fireball", "fire air")}")
        print("record_spell(\"Dark Magic\", \"shadow\"): " +
              f"{record_spell("Dark Magic", "shadow")}")
    except Exception as e:
        print(e)


def late_import() -> None:
    try:
        print("\nTesting late import technique:")
        from alchemy.grimoire.spellbook import record_spell
        print("record_spell(\"Lightning\", \"air\"): " +
              f"{record_spell("Lightning", "air")}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")
    test_validation()
    test_spell()
    late_import()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
