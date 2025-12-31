
def perform_move(move_name, attacker, defender):
    match move_name:
        case "ATTACK":
            damage = max(1, attacker.attack - defender.defense)
            defender.hp -= damage
            return f"{attacker.name} attacks for {damage} damage"

        case "DEFEND":
            attacker.defense += 2
            return f"{attacker.name} raises his defense"

        case _:
            return "pass"