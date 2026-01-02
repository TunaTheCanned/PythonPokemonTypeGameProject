import json
import pygame
from source.creature import Creature

def load_creature(path):

    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"{path}: not found")
        pygame.quit()
        raise SystemExit
    except json.decoder.JSONDecodeError:
        print(f"{path}: invalid json")
        pygame.quit()
        raise SystemExit

    creatures = []
    for creature in data:
        try:
            sprite = pygame.image.load(creature['sprite']).convert_alpha()
            creatures.append(Creature(creature['name'], creature['hp'], creature['attack'], creature['defense'], creature['evasion'], creature['moves'], sprite))
        except FileNotFoundError:
            print(f"{creature['sprite']}: not found")


    return creatures


