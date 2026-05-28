# Credit to ShadowDev7 for the original code, which was adapted and expanded upon for this project.
# License: MIT License

import argparse

def calculate(parent1: str, parent2: str):
    gametes1 = parent1
    gametes2 = parent2

    total = 0
    result = []

    gametes_AA = 0
    gametes_aa = 0
    gametes_Aa = 0

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
        },
    }


def main():
    valid_combinations = ["aa", "Aa", "aA", "AA"]

    parser = argparse.ArgumentParser(
        prog="Punnett Square Calculator",
        description="Cross allele sequences using a Punnett square",
    )

    parser.add_argument(
        "-p1", "--parent1",
        type=str,
        required=True,
        help="Parent 1 sequence (AA, Aa, aA, or aa)",
    )

    parser.add_argument(
        "-p2", "--parent2",
        type=str,
        required=True,
        help="Parent 2 sequence (AA, Aa, aA, or aa)",
    )

    parser.add_argument(
        "--phenotype",
        action="store_true",
        help="Show only the phenotype",
    )

    parser.add_argument(
        "--genotype",
        action="store_true",
        help="Show only the genotype",
    )

    parser.add_argument(
        "--output",
        type=str,
        required=False,
        help="Write the result to another file",
    )

    args = parser.parse_args()

    if len(args.parent1) != 2 or len(args.parent2) != 2:
        parser.error("Each parent must contain exactly TWO alleles (e.g. Aa)")

    if args.parent1 not in valid_combinations or args.parent2 not in valid_combinations:
        parser.error("Each parent must be one of: AA, Aa, aA, aa")

    results = calculate(args.parent1, args.parent2)

    output_parts = []

    if args.genotype and not args.phenotype:
        output_parts.append(
            "\nGenotype:\n"
            f"AA: {results['genotype']['AA']:.2f}%\n"
            f"Aa: {results['genotype']['Aa']:.2f}%\n"
            f"aa: {results['genotype']['aa']:.2f}%"
        )
    elif args.phenotype and not args.genotype:
        output_parts.append(
            "\nPhenotype:\n"
            f"A: {results['phenotype']['A']:.2f}%\n"
            f"a: {results['phenotype']['a']:.2f}%"
        )
    else:
        output_parts.append(
            "\nGenotype:\n"
            f"AA: {results['genotype']['AA']:.2f}%\n"
            f"Aa: {results['genotype']['Aa']:.2f}%\n"
            f"aa: {results['genotype']['aa']:.2f}%"
        )
        output_parts.append(
            "\nPhenotype:\n"
            f"A: {results['phenotype']['A']:.2f}%\n"
            f"a: {results['phenotype']['a']:.2f}%"
        )

    output_parts.append(f"\nCombinations: {results['combinations']}")

    output_text = "\n".join(output_parts)

    print(output_text)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(output_text)
        print(f"\n[!] The result was written to: {args.output}")


if __name__ == "__main__":
    main()