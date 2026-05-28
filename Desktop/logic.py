import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).with_name(".matplotlib_cache")))

import matplotlib.pyplot as plt

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



def graphs(results: dict): # Made with Codex
    genotype = results["genotype"]
    phenotype = results["phenotype"]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    fig.suptitle("Punnett Square Results")

    axes[0].bar(genotype.keys(), genotype.values(), color=["#4e79a7", "#f28e2b", "#e15759"])
    axes[0].set_title("Genotype Distribution")
    axes[0].set_xlabel("Genotype")
    axes[0].set_ylabel("Percentage")
    axes[0].set_ylim(0, 100)

    axes[1].bar(phenotype.keys(), phenotype.values(), color=["#59a14f", "#b07aa1"])
    axes[1].set_title("Phenotype Distribution")
    axes[1].set_xlabel("Phenotype")
    axes[1].set_ylabel("Percentage")
    axes[1].set_ylim(0, 100)

    for axis in axes:
        for bar in axis.patches:
            height = bar.get_height()
            axis.text(
                bar.get_x() + bar.get_width() / 2,
                height + 1,
                f"{height:.1f}%",
                ha="center",
                va="bottom",
            )

    plt.tight_layout()
    plt.show()

def main():
    pass 

if __name__ == "__main__":
    main()
