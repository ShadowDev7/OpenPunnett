def calculate(parent1: str, parent2: str):
    gametes1 = list(parent1)
    gametes2 = list(parent2)

    total = 0
    result: list[str] = []

    gametes_AA: int = 0
    gametes_aa: int = 0
    gametes_Aa: int = 0

    for p1 in gametes1:
        for p2 in gametes2:
            combination = "".join(sorted(p1 + p2))
            
            total += 1
            result.append(combination)

            if combination == "AA":
                gametes_AA += 1
            elif combination == "aa":
                gametes_aa += 1
            elif combination == "Aa":
                gametes_Aa += 1

    phenotype_A: int = gametes_AA + gametes_Aa
    phenotype_a: int = gametes_aa

    return {
        "total": total,
        "combinations": result,
        "genotype": {
            "AA": (gametes_AA / total) * 100,
            "Aa": (gametes_Aa / total) * 100,
            "aa": (gametes_aa / total) * 100,
        },
        "phenotype": {
            "A": (phenotype_A / total) * 100,
            "a": (phenotype_a / total) * 100,
        },
    }


def main():
    pass 

if __name__ == "__main__":
    main()
