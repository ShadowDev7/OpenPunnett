# Punnett Square Calculator

A simple Python CLI tool for calculating genotype and phenotype percentages using a Punnett square.

## Features

- Calculates genotype percentages
- Calculates phenotype percentages
- Shows allele combinations
- Supports command-line usage
- Can export results to a file

## Requirements

- Python 3.x (2.7 won't work, trust me)

## Installation

Clone the repository:

```bash
git clone https://github.com/ShadowDev7/punnett-square-calculator.git
cd punnett-square-calculator
```

## Usage

Run the script with two parent genotypes:

```bash
python main.py -p1 Aa -p2 Aa
```

## Format 

Each parent must be given as a two-letter genotype:

- `AA`
- `Aa`
- `aA`
- `aa`

(Now this knolwedge comes from what I learned in School so don't except me to be 100% correct. I do not have a PhD)

Example:

```bash
python main.py -p1 AA -p2 Aa
```

## Commands

| Command | Description |
|---------|-------------|
| `-p1`, `--parent1` | Parent 1 genotype (`AA`, `Aa`, `aA`, or `aa`) |
| `-p2`, `--parent2` | Parent 2 genotype (`AA`, `Aa`, `aA`, or `aa`) |
| `--genotype` | Show only genotype results |
| `--phenotype` | Show only phenotype results |
| `--output <file>` | Save the result to a file |

## Examples

Show everything:

```bash
python main.py -p1 Aa -p2 Aa
```

Show only genotype:

```bash
python main.py -p1 Aa -p2 Aa --genotype
```

Show only phenotype:

```bash
python main.py -p1 Aa -p2 Aa --phenotype
```

Save output to a file:

```bash
python main.py -p1 Aa -p2 Aa --output result.txt
```

## Example Output

```text
Genotype:
AA: 25.00%
Aa: 50.00%
aa: 25.00%

Phenotype:
A: 75.00%
a: 25.00%

Combinations: ['AA', 'Aa', 'Aa', 'aa']
```

## Valid Inputs

Accepted parent values:

- `AA`
- `Aa`
- `aA`
- `aa`

## Biology Notes

- `A` is treated as the dominant allele
- `a` is treated as the recessive allele
- `AA` and `Aa` produce the dominant phenotype
- `aa` produces the recessive phenotype

## Notes

This tool is designed for simple one-gene Punnett square exercises and educational use. In addition, this manual applies to the Greek version too

## License

MIT
