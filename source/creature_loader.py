import json
import pygame
from source.creature import Creature

def load_creature(path):
    with open(path, 'r') as json_file:
        data = json.load(json_file)

    creatures = []
    for creature in data:
        sprite = pygame.image.load(creature['sprite']).convert_alpha()
        creatures.append(Creature(creature['name'], creature['hp'], creature['attack'], creature['defense'], creature['moves'], sprite))

    return creatures


