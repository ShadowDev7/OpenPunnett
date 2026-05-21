def calculate_punnett_square(parent1: str, parent2: str) -> list:
    gametes1 = list(parent1)
    gametes2 = list(parent2)
    offspring = [] # List to store the possible offspring genotypes (Απόγονοί)
    
    gametes_aa: int = 0
    gametes_Aa: int = 0
    gametes_AA: int = 0
    
    for g1 in gametes1:
        for g2 in gametes2:
            offspring.append(g1 + g2)
            combination = ''.join(sorted(g1 + g2))
            if combination == 'aa':
                gametes_aa += 1
            elif combination == 'Aa':
                gametes_Aa += 1
            elif combination == 'AA':
                gametes_AA += 1
                




