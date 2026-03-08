def healing_potion() -> str:
    from .elements import create_fire, create_water
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    from .elements import create_earth, create_fire
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    return (f"Invisibility potion brewed with {create_air()}"
            f"and {create_water()}")


def wisdom_potion() -> str:
    import elements
    return ("Wisdom potion brewed with all elements: "
            f"{elements.create_air()} {elements.create_earth()} "
            f"{elements.create_water()} {elements.create_fire()}")
