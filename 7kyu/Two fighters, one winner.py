def declare_winner(fighter1, fighter2, first_attacker):
    current_attacker = fighter1 if first_attacker == fighter1.name else fighter2

    while fighter1.health > 0 and fighter2.health > 0:
        
        if current_attacker == fighter1:
            fighter2.health -= fighter1.damage_per_attack
        else:
            fighter1.health -= fighter2.damage_per_attack
            
        current_attacker = fighter2 if current_attacker == fighter1 else fighter1
        
    if fighter1.health <= 0:
        return fighter2.name 
    else:
        return fighter1.name
