def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set = set(["first_kill", "level_10",
                      "treasure_hunter", "speed_demon"])
    bob: set = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie: set = set(["level_10", "treasure_hunter",
                        "boss_slayer", "speed_demon", "perfectionist"])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")
    unique: set = charlie.union(bob, alice)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")

    common: set = alice.intersection(bob, charlie)
    print(f"Common to all players: {common}")
    alice_rare = alice.difference(bob, charlie)
    bob_rare = bob.difference(alice, charlie)
    charlie_rare = charlie.difference(alice, bob)
    rare = alice_rare.union(bob_rare, charlie_rare)
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    alice_unique: set = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
