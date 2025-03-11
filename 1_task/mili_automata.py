"""Import base modules"""
from base_automata import BaseAutomata

class MiliAutomata(BaseAutomata):
    """Realisation of Mili Automata"""
    def __init__(self, states: list[str],
                 initial_state: str,
                 alphabet: list[str],
                 table:dict[str, dict[str, list[str]]]) -> None:
        super().__init__(states, initial_state, alphabet)
        self.table = table

    def step(self, inp: str):
        """Machine step"""
        self.state, reaction = self.table[self.state][inp]
        return reaction
