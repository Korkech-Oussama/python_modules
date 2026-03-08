from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def validate(self) -> bool:
        return isinstance(self.attack, int) and self.attack > 0 and \
                isinstance(self.health, int) and self.health > 0

    def play(self, game_state: dict) -> dict:
        play_info: dict = {'card_played': self.name,
                            'mana_used': game_state,
                            'effect': 'Creature summoned to battlefield'
                            }
        return play_info

    def attack_target(self, target) -> dict:
        attack_res: dict = {'attacker': self.name,
                            'target': target,
                            'damage_dealt': self.attack,
                            'combat_resolved': self.validate()}
        return attack_res
    def get_card_info(self) -> dict:
        creature_infos: dict = {'type': 'Creature', 'attack': self.attack, 'health': self.health}
        all_infos = super().get_card_info() | creature_infos
        return all_infos

