from typing import Set, Dict, List, Optional, Tuple
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)  # Make the class immutable and automatically implement __hash__
class State:
    name: str
    is_final: bool = False

class DFA:
    def __init__(self, alphabet: Set[str]):
        self.alphabet = alphabet
        self.states: Set[State] = set()
        self.transitions: Dict[Tuple[State, str], State] = {}
        self.initial_state: Optional[State] = None
        self.final_states: Set[State] = set()

    def add_state(self, state: State) -> None:
        self.states.add(state)
        if state.is_final:
            self.final_states.add(state)

    def add_transition(self, from_state: State, symbol: str, to_state: State) -> None:
        if symbol not in self.alphabet:
            raise ValueError(f"Symbol {symbol} not in alphabet")
        self.transitions[(from_state, symbol)] = to_state

    def set_initial_state(self, state: State) -> None:
        if state not in self.states:
            raise ValueError("State not in DFA")
        self.initial_state = state

    def process_sequence(self, sequence: str) -> bool:
        if not self.initial_state:
            raise ValueError("No initial state set")
        
        current_state = self.initial_state
        for symbol in sequence:
            if (current_state, symbol) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, symbol)]
        
        return current_state in self.final_states

class PDA:
    def __init__(self, input_alphabet: Set[str], stack_alphabet: Set[str]):
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.states: Set[State] = set()
        self.transitions: Dict[Tuple[State, str, str], List[Tuple[State, str]]] = {}
        self.initial_state: Optional[State] = None
        self.final_states: Set[State] = set()
        self.stack: List[str] = []

    def add_state(self, state: State) -> None:
        self.states.add(state)
        if state.is_final:
            self.final_states.add(state)

    def add_transition(self, from_state: State, input_symbol: str, 
                      stack_symbol: str, to_state: State, 
                      stack_push: str) -> None:
        if input_symbol not in self.input_alphabet:
            raise ValueError(f"Input symbol {input_symbol} not in alphabet")
        if stack_symbol not in self.stack_alphabet:
            raise ValueError(f"Stack symbol {stack_symbol} not in stack alphabet")
        
        key = (from_state, input_symbol, stack_symbol)
        if key not in self.transitions:
            self.transitions[key] = []
        self.transitions[key].append((to_state, stack_push))

    def process_sequence(self, sequence: str) -> bool:
        if not self.initial_state:
            raise ValueError("No initial state set")
        
        self.stack = ['Z']  # Initial stack symbol
        current_state = self.initial_state
        
        for symbol in sequence:
            stack_top = self.stack[-1]
            key = (current_state, symbol, stack_top)
            
            if key not in self.transitions:
                return False
                
            # Get the first valid transition
            next_state, stack_action = self.transitions[key][0]
            
            # Update stack
            if stack_action == 'ε':  # Pop
                self.stack.pop()
            elif stack_action != 'ε':  # Push
                self.stack.append(stack_action)
                
            current_state = next_state
        
        return current_state in self.final_states and len(self.stack) == 1 and self.stack[0] == 'Z' 