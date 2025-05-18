import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List
import seaborn as sns

class MotifPlotter:
    def __init__(self):
        plt.style.use('default')
        self.colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

    def plot_motif_positions(self, sequence_name: str, positions: List[int], 
                           sequence_length: int, motif_length: int):
        """Plot motif positions along a sequence."""
        plt.figure(figsize=(12, 2))
        
        # Create a binary array for motif positions
        motif_array = np.zeros(sequence_length)
        for pos in positions:
            motif_array[pos:pos + motif_length] = 1
        
        plt.plot(motif_array, color=self.colors[0])
        plt.title(f"Motif Positions in {sequence_name}")
        plt.xlabel("Position")
        plt.ylabel("Motif Present")
        plt.yticks([0, 1])
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        return plt.gcf()

    def plot_motif_frequencies(self, frequencies: Dict[str, float]):
        """Plot motif frequencies across different sequences."""
        plt.figure(figsize=(10, 6))
        
        sequences = list(frequencies.keys())
        values = list(frequencies.values())
        
        plt.bar(sequences, values, color=self.colors[1])
        plt.title("Motif Frequencies Across Sequences")
        plt.xlabel("Sequence")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        return plt.gcf()

    def plot_motif_distribution(self, all_positions: Dict[str, List[int]]):
        """Plot the distribution of motif positions across all sequences."""
        plt.figure(figsize=(10, 6))
        
        # Flatten all positions
        all_pos = []
        for positions in all_positions.values():
            all_pos.extend(positions)
        
        plt.hist(all_pos, bins=50, color=self.colors[2])
        plt.title("Distribution of Motif Positions")
        plt.xlabel("Position")
        plt.ylabel("Count")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        return plt.gcf()

    def save_plot(self, figure, filename: str):
        """Save the current plot to a file."""
        figure.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close(figure) 