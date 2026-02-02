def ft_count_harvest_recursive(days=None):
    # 1. Check if we need to ask for input
    if days is None:
        days = int(input("Days until harvest: "))
    # 3. Base case
    if days < 1:
        return
    ft_count_harvest_recursive(days - 1)
    print("Day", days)
