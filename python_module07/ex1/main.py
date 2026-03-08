from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from typing import List
if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===\n")

    creature: CreatureCard = CreatureCard("Fire Dragon", 3,
                                          "Legendary", 2, 5)
    spell: SpellCard = SpellCard('Lightning Bolt', 6, "Legendary",
                                 "Deal 3 damage to target")
    artifact: ArtifactCard = ArtifactCard('Mana Crystal',3, "legendary", 8,
                                          "Permanent: +1 mana per turn")

    cards: List[Card] = [creature, spell, artifact]
    deck: Deck = Deck()
    for card in cards:
        deck.add_card(card)

    print("Building deck with different card types...")
    print(f"Deck stats:{deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    card1 = deck.draw_card()
    print(f"Play result: {card1.play(3)}")

    card2 = deck.draw_card()
    print(f"Play result: {card2.play(2)}")

    card3 = deck.draw_card()
    print(f"Play result: {card3.play(5)}")

    print("\nPolymorphism in action: Same interface, different card behaviors!")
