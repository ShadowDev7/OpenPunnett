// Created by ShadowDev7
/* To clairfy, as I am doing this, 
I don't now a lot about TypeScript, I come from C and Python. 
Probably will in the future. When I reach there I will delete this comment. */

// So I searched on Google whats an interface, it's apparently like a struct in C. I guess?
export interface GenotypeRatio {
  AA: number;
  Aa: number;
  aa: number;
}

export interface PhenotypeRatio {
  A: number;
  a: number;
}

export interface GeneticCrossResult {
  total: number;
  combinations: string[];
  genotype: GenotypeRatio;
  phenotype: PhenotypeRatio;
}

function calculate(parent1: string, parent2: string): GeneticCrossResult {
  const gametes1: string = parent1;
  const gametes2: string = parent2;

  let total: number = 0;
  // We can use Array<T> but string[] is more recommended apparently?
  const results: string[] = [];

  let gametes_Aa: number = 0;
  let gametes_AA: number = 0;
  let gametes_aa: number = 0;

  // The tool is more for students and simple stuff. Threfore, since it's 2 characters, O(n^2) is fine
  for (const p1 of gametes1) {
    for (const p2 of gametes2) {
      // Normalizes "aA" to "Aa"
      const combination: string = [p1, p2].sort().join("");

      total++;
      results.push(combination);

      if (combination === "AA") {
        gametes_AA++;
      } else if (combination === "aa") {
        gametes_aa++;
      } else if (combination === "Aa") {
        gametes_Aa++;
      }
    }
  }

  const phenotype_A: number = gametes_AA + gametes_Aa;
  const phenotype_a: number = gametes_aa;

  // Prevent division by zero if empty strings are passed
  const safeTotal = total || 1;

  // Ah wow simillar to python?
  return {
    total,
    combinations: results,
    genotype: {
      AA: (gametes_AA / safeTotal) * 100,
      Aa: (gametes_Aa / safeTotal) * 100,
      aa: (gametes_aa / safeTotal) * 100,
    },
    phenotype: {
      A: (phenotype_A / safeTotal) * 100,
      a: (phenotype_a / safeTotal) * 100,
    },
  };
}
