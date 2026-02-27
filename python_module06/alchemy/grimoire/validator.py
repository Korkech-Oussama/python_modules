def validate_ingredients(ingredients: str) -> str:
    lst_ingedient : list[str] = ["fire", "water", "earth", "air"]
    for item in lst_ingedient:
        if item in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"