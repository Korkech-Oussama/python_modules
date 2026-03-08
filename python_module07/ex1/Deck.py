from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random
from typing import List


class Deck:

    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        card: Card = random.choice(self.cards)
        print(f"\nDrew: {card.name} ({type(card).__name__})")
        self.cards.remove(card)
        return card

    def get_deck_stats(self) -> dict:
        creature_count: int = sum(1 for card in self.cards
                                   if isinstance(card, CreatureCard))
        spells_count: int = sum(1 for card in self.cards
                                   if isinstance(card, SpellCard))
        artifact_count: int = sum(1 for card in self.cards
                                   if isinstance(card, ArtifactCard))
        total_cost: int = sum(card.cost for card in self.cards)
        if self.cards:
            avg:float = round(total_cost / len(self.cards), 1)
        else:
            avg:float = 0.0
        infos: dict = {'total_cards': len(self.cards),
                       'creatures': creature_count,
                       'spells': spells_count,
                       'artifacts': artifact_count,
                       'avg_cost': avg}
        return infos
