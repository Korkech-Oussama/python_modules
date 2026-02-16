import sys


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    ac = len(sys.argv)

    if ac > 1:
        i = 0
        mylist = []
        [mylist.append(p.split(":")) for p in sys.argv[1:]]
        my_dict = {name: int(quantity) for name, quantity in mylist}
        for value in my_dict.values():
            i += value
        unique: set = {key for key in my_dict.keys()}
        unique_types: int = len(unique)
        print(f"Total items in inventory: {i}")
        print(f"Unique item types: {unique_types}\n")

        print("=== Current Inventory ===")
        for key, value in my_dict.items():
            print(f"{key}: {value} units ({value / i * 100:.2f}%)")

        print("\n=== Inventory Statistics ===")
        max_val: int = -1
        min_val: int = i
        for key, value in my_dict.items():
            if value > max_val:
                max_val = value
                max_item: str = key
            if value < min_val:
                min_val = value
                min_item: str = key

        print(f"Most abundant: {max_item} ({max_val} units)")
        print(f"Most abundant: {min_item} ({min_val} units)\n")

        print("=== Item Categories ===")
        moderate: dict = {}
        scarce: dict = {}
        for key, value in my_dict.items():
            if value >= 5:
                moderate.update({key: value})
            elif value < 5:
                scarce.update({key: value})

        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}\n")

        print("=== Management Suggestions ===")
        restock: list = []
        for key, value in my_dict.items():
            if value == 1:
                restock.append(key)
        print(f"Restock needed: {restock}")

        print("=== Dictionary Properties Demo ===")
        print("Dictionary keys: ", end="")
        keys_list: list[str] = list(my_dict.keys())
        print(*keys_list, sep=", ")
        print("Dictionary values: ", end="")
        values_list: list[int] = list(my_dict.values())
        print(*values_list, sep=", ")
        target: str = 'sword'
        is_in_dict: bool = my_dict.get(target) is not None
        print(f"Sample lookup - '{target}' in inventory: {is_in_dict}")


if __name__ == "__main__":
    ft_inventory_system()
