from typing import List, Set, Dict, Optional
from Bio import SeqIO
from Bio.Seq import Seq
from .automata import DFA, State
import numpy as np
from tqdm import tqdm

class SequenceProcessor:
    def __init__(self):
        self.dna_alphabet = {'A', 'T', 'C', 'G'}
        self.motif_dfa: Optional[DFA] = None

    def load_sequence(self, file_path: str) -> List[Seq]:
        """Load DNA sequences from a FASTA file."""
        sequences = []
        for record in SeqIO.parse(file_path, "fasta"):
            sequences.append(record.seq)
        return sequences

    def create_motif_dfa(self, motif: str) -> DFA:
        """Create a DFA for a specific DNA motif."""
        dfa = DFA(self.dna_alphabet)
        
        # Create states for each position in the motif
        states = []
        for i in range(len(motif) + 1):
            state = State(f"q{i}", i == len(motif))
            states.append(state)
            dfa.add_state(state)
        
        # Set initial state
        dfa.set_initial_state(states[0])
        
        # Add transitions
        for i in range(len(motif)):
            # Add transition for the correct nucleotide
            dfa.add_transition(states[i], motif[i], states[i + 1])
            
            # Add transitions for other nucleotides (back to start)
            for nt in self.dna_alphabet - {motif[i]}:
                dfa.add_transition(states[i], nt, states[0])
        
        self.motif_dfa = dfa
        return dfa

    def find_motif_positions(self, sequence: Seq, motif: str) -> List[int]:
        """Find all positions where the motif occurs in the sequence."""
        if not self.motif_dfa:
            self.create_motif_dfa(motif)
        
        positions = []
        window_size = len(motif)
        
        for i in range(len(sequence) - window_size + 1):
            window = str(sequence[i:i + window_size])
            if self.motif_dfa.process_sequence(window):
                positions.append(i)
        
        return positions

    def find_motifs_in_sequences(self, sequences: List[Seq], motif: str) -> Dict[str, List[int]]:
        """Find motif positions in multiple sequences."""
        results = {}
        for i, seq in enumerate(tqdm(sequences, desc="Processing sequences")):
            positions = self.find_motif_positions(seq, motif)
            results[f"sequence_{i}"] = positions
        return results

    def calculate_motif_frequency(self, sequences: List[Seq], motif: str) -> float:
        """Calculate the frequency of a motif across all sequences."""
        total_occurrences = 0
        total_positions = 0
        
        for seq in sequences:
            positions = self.find_motif_positions(seq, motif)
            total_occurrences += len(positions)
            total_positions += len(seq) - len(motif) + 1
        
        return total_occurrences / total_positions if total_positions > 0 else 0.0 