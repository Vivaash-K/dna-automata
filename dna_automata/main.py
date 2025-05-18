import argparse
from pathlib import Path
from core.sequence_processor import SequenceProcessor
from visualization.plotter import MotifPlotter

def main():
    parser = argparse.ArgumentParser(description='DNA Sequence Analysis using Automata')
    parser.add_argument('--input', required=True, help='Input FASTA file path')
    parser.add_argument('--motif', required=True, help='DNA motif to search for')
    parser.add_argument('--output', default='results', help='Output directory for results')
    args = parser.parse_args()

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)

    # Initialize components
    processor = SequenceProcessor()
    plotter = MotifPlotter()

    # Load sequences
    print(f"Loading sequences from {args.input}...")
    sequences = processor.load_sequence(args.input)

    # Find motif positions
    print(f"Searching for motif '{args.motif}'...")
    motif_positions = processor.find_motifs_in_sequences(sequences, args.motif)

    # Calculate frequencies
    frequencies = {}
    for seq_id, positions in motif_positions.items():
        frequencies[seq_id] = len(positions) / len(sequences[0])

    # Generate and save plots
    print("Generating visualizations...")
    
    # Plot motif positions for first sequence
    first_seq = list(motif_positions.keys())[0]
    fig = plotter.plot_motif_positions(
        first_seq,
        motif_positions[first_seq],
        len(sequences[0]),
        len(args.motif)
    )
    plotter.save_plot(fig, output_dir / "motif_positions.png")

    # Plot frequencies
    fig = plotter.plot_motif_frequencies(frequencies)
    plotter.save_plot(fig, output_dir / "motif_frequencies.png")

    # Plot distribution
    fig = plotter.plot_motif_distribution(motif_positions)
    plotter.save_plot(fig, output_dir / "motif_distribution.png")

    print(f"Analysis complete. Results saved to {output_dir}")

if __name__ == "__main__":
    main() 