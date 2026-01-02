
# def poison(damage, turns):
#     return {"type": "POISON", "damage": damage, "turns_left": turns}

def perform_move(move_name, attacker, defender):
    match move_name:
        case "ATTACK":
            damage = max(1, attacker.attack - defender.defense)
            defender -= damage
            return f"{attacker.name} attacks for {damage} damage"

        case "DEFEND":
            attacker.defense += 2
            return f"{attacker.name} raises his defense"

        case "WEAKEN":
            defender /= 1.2
            return f"{defender.name} weakens"

        case "FIGHTING STANCE":
            attacker *= 1.1
            return f"{attacker.name} adopts a fighting stance"

        case "POISON":
            defender.status_effects.append({"type": "POISON", "damage": 10, "turns_left": 3})
            return f"{attacker.name} poisons {defender.name}"

        case _:
            return "default case"