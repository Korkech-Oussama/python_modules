def test_validation() -> None:
    from alchemy.grimoire.validator import validate_ingredients
    print(f"validate_ingredients(\"fire air\"):" +
          f"{validate_ingredients("fire air")}")
    print(f"validate_ingredients(\"dragon scales\"):" +
          f"{validate_ingredients("dragon scales")}")


def test_spell() -> None:
    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting spell recording with validation:")
    print(f"record_spell(\"Fireball\", \"fire air\"): {record_spell("Fireball", "fire air")}")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {record_spell("Dark Magic", "shadow")}")

def late_import() -> None:
    print("\nTesting late import technique:")
    from alchemy.grimoire.spellbook import record_spell
    print(f"record_spell(\"Lightning\", \"air\"): {record_spell("Lightning", "air")}")

if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")
    test_validation()
    test_spell()
    late_import()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")