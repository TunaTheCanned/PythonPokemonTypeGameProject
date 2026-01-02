
class Creature:
    def __init__(self, name, hp, attack, defense, moves, sprite):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves
        self.sprite = sprite
        self.status_effects = []


    def __isub__(self, damage):
        self.hp -= int(damage)
        if self.hp <= 0:
            self.hp = 0
        return self

    def __add__(self, heal):
        self.hp += int(heal)
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
        return self

    def __imul__(self, factor):
        self.attack = int(self.attack * factor)
        self.defense = int(self.defense * factor)
        return self

    def __itruediv__(self, factor):
        self.attack = int(self.attack / factor)
        self.defense = int(self.defense / factor)
        return self

    def copy(self):
        return Creature(self.name, self.max_hp, self.attack, self.defense, self.moves, self.sprite)
