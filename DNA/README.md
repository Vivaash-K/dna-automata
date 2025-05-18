# DNA Sequence Analysis using Automata Theory

This project implements a DNA sequence analysis system using automata theory, specifically focusing on efficient motif detection and pattern recognition in DNA sequences.

## Features

- Deterministic Finite Automata (DFA) for motif detection
- Pushdown Automata (PDA) for nested structure recognition
- Efficient sequence processing and pattern matching
- Visualization tools for analyzing results
- Support for large-scale sequence analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vivaash-K/dna-automata.git
cd dna-automata
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The system can be used to analyze DNA sequences and detect specific motifs. Here's a basic example:

```bash
python dna_automata/main.py --input sequences.fasta --motif "ATCG" --output results
```

### Arguments

- `--input`: Path to the input FASTA file containing DNA sequences
- `--motif`: The DNA motif to search for (e.g., "ATCG")
- `--output`: Directory to save the analysis results (default: "results")

### Output

The system generates several visualization files in the output directory:
- `motif_positions.png`: Shows the positions of the motif in the first sequence
- `motif_frequencies.png`: Displays the frequency of the motif across all sequences
- `motif_distribution.png`: Shows the distribution of motif positions

## Project Structure

```
dna_automata/
├── core/
│   ├── automata.py      # DFA and PDA implementations
│   └── sequence_processor.py  # Sequence processing utilities
├── visualization/
│   └── plotter.py       # Visualization tools
├── main.py              # Main script
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Testing with Public Datasets

The system can be tested with publicly available genomic datasets:

1. NCBI GenBank: Download FASTA files of interest
2. UCSC Genome Browser: Access various genome sequences
3. Ensembl: Download DNA sequences for different organisms

Example workflow:
1. Download a FASTA file from any of these sources
2. Run the analysis with your motif of interest
3. Analyze the results using the generated visualizations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 