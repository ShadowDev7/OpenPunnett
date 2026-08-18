# License  

""" 
MIT License

Copyright (c) 2026 ShadowDev7 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse

def calculate(parent1: str, parent2: str):
    gametes1: str = parent1
    gametes2: str = parent2

    total: int = 0
    result: list[str] = []

    gametes_AA: int = 0
    gametes_aa: int = 0
    gametes_Aa: int = 0

    # Since its mainly two characters, a nested loop is fine
    for p1 in gametes1:
        for p2 in gametes2:
            combination: str = "".join(sorted(p1 + p2))
            
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
    valid_combinations: list[str] = ["aa", "Aa", "aA", "AA"]

    parser = argparse.ArgumentParser(
        prog="",
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

    output_parts: list = []

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
