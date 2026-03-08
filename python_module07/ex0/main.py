from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"CreatureCard Info:\n{creature.get_card_info()}")

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"playable: {creature.is_playable(6)}")
    print(f"Play result: {creature.play(6)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {creature.attack_target("Goblin Warrior")}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Play result: {creature.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")
