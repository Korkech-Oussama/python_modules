def absolute_imports() -> None:
    print("Testing Absolute Imports (from basic.py):")
    try:
        from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
        print(f"Lead_to_gold(): {lead_to_gold()}")
        print(f"stone_to_gem(): {stone_to_gem()}")
    except Exception as e:
        print(e)


def relative_import() -> None:
    print("\nTesting Relative Imports (from advanced.py):")
    try:
        from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life  # noqa : F401
        print(f"philosophers_stone(): {philosophers_stone()}")
        print(f"elixir_of_life(): {elixir_of_life()}")
    except Exception as e:
        print(e)


def package_access() -> None:
    print("\nTesting Package Access:")
    try:
        import alchemy
        print("alchemy.transmutation.lead_to_gold():" +
              f"{alchemy.transmutation.lead_to_gold()}")
        print("alchemy.transmutation.philosophers_stone():" +
              f"{alchemy.transmutation.philosophers_stone()}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===\n")

    absolute_imports()
    relative_import()
    package_access()

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
