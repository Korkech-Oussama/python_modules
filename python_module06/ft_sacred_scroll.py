def direct_import() -> None:
    import alchemy.elements
    print("Testing direct module access:")

    try:
        print("alchemy.elements.create_fire(): "
              f"{alchemy.elements.create_fire()}")
        print("alchemy.elements.create_water(): "
              f"{alchemy.elements.create_water()}")
        print("alchemy.elements.create_earth(): "
              f"{alchemy.elements.create_earth()}")
        print("alchemy.elements.create_air(): "
              f"{alchemy.elements.create_air()}")
    except Exception as e:
        print(e)


def package_import() -> None:
    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        import alchemy
        try:
            print(f"alchemy.create_fire(): {alchemy.create_fire()}")
        except AttributeError as e:
            print(e)
        try:
            print(f"alchemy.create_water(): {alchemy.create_water()}")
        except AttributeError as e:
            print(e)
        try:
            print(f"alchemy.create_air(): {alchemy.create_air()}")
        except AttributeError:
            print("alchemy.create_air(): AttributeError - not exposed")
        try:
            print(f"alchemy.create_earth(): {alchemy.create_earth()}")
        except AttributeError:
            print("alchemy.create_earth(): AttributeError - not exposed")
    except Exception as e:
        print(type(e))


def package_metadate() -> None:
    print("\nPackage metadata:")
    try:
        import alchemy
        print(f"Version: {alchemy.__version__}")
        print(f"Author: {alchemy.__author__}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")

    direct_import()
    package_import()
    package_metadate()
