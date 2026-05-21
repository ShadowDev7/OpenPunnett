# Credit to ShadowDev7 for the 

import argparse
def calculate(parent1: str, parent2: str):
    gametes1 = list(parent1)
    gametes2 = list(parent2)

    total = 0
    result = []

    gametes_AA = 0
    gametes_aa = 0
    gametes_Aa = 0

    for p1 in gametes1:
        for p2 in gametes2:
            combination = "".join(sorted(p1 + p2, reverse=True))

            total += 1
            result.append(combination)

            if combination == "AA":
                gametes_AA += 1
            elif combination == "aa":
                gametes_aa += 1
            elif combination == "Aa":
                gametes_Aa += 1

    phenotype_A = gametes_AA + gametes_Aa
    phenotype_a = gametes_aa

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
        }
    }


def main():
    valid_combinations = ["aa", "Aa", "aA", "AA"]

    parser = argparse.ArgumentParser(
        prog="Διασταύρωση Αλληλουχίων",
        description="Διασταύρωση Αλληλουχιών με τον πίνακα του Punnett"
    )

    parser.add_argument(
        "-p1", "--parent1",
        type=str,
        required=True,
        help="Γονέας 1 Αλληλουχία (AA, Aa, or aa)"
    )

    parser.add_argument(
        "-p2", "--parent2",
        type=str,
        required=True,
        help="Γονέας 2 Αλληλουχία (AA, Aa, or aa)"
    )

    parser.add_argument(
        "--phenotype",
        action="store_true",
        help="Δείχνει μόνο τον φαινότυπο"
    )

    parser.add_argument(
        "--genotype",
        action="store_true",
        help="Δείχνει μόνο τον γονότυπο"
    )

    parser.add_argument(
        "--output",
        type=str,
        required=False,
        help="Γράψε το αποτέλεσμα σε ένα άλλο αρχείο"
    )

    args = parser.parse_args()

    if len(args.parent1) != 2 or len(args.parent2) != 2:
        parser.error("Κάθε γονέας πρέπει να περιέχει ακριβώς ΔΥΟ γονίδια (e.g. Aa)")

    if args.parent1 not in valid_combinations or args.parent2 not in valid_combinations:
        parser.error("Κάθε γονέας πρέπει να είναι: AA, Aa, aA, aa")

    results = calculate(args.parent1, args.parent2)

    output_parts = []

    if args.genotype and not args.phenotype:
        output_parts.append(
            "\nΓονότυπος:\n"
            f"AA: {results['genotype']['AA']:.2f}%\n"
            f"Aa: {results['genotype']['Aa']:.2f}%\n"
            f"aa: {results['genotype']['aa']:.2f}%"
        )
    elif args.phenotype and not args.genotype:
        output_parts.append(
            "\nΦαινότυπος:\n"
            f"A: {results['phenotype']['A']:.2f}%\n"
            f"a: {results['phenotype']['a']:.2f}%"
        )
    else:
        output_parts.append(
            "\nΓονότυπος:\n"
            f"AA: {results['genotype']['AA']:.2f}%\n"
            f"Aa: {results['genotype']['Aa']:.2f}%\n"
            f"aa: {results['genotype']['aa']:.2f}%"
        )
        output_parts.append(
            "\nΦαινότυπος:\n"
            f"A: {results['phenotype']['A']:.2f}%\n"
            f"a: {results['phenotype']['a']:.2f}%"
        )

    output_parts.append(f"\nΕνώσεις: {results['combinations']}")

    output_text = "\n".join(output_parts)

    print(output_text)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(output_text)
        print(f"\n[!] Το αποτέλεσμα γράφτηκε στο αρχείο: {args.output}")


if __name__ == "__main__":
    main()
