
class Creature:
    def __init__(self, name, hp, attack, defense, moves, sprite):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves
        self.sprite = sprite

    def copy(self):
        return Creature(self.name, self.max_hp, self.attack, self.defense, self.moves, self.sprite)
