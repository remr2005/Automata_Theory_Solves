"""Import base modules"""
from base_automata import BaseAutomata

class MureAutomata(BaseAutomata):
    """Realisation of Mili Automata"""
    def __init__(self, states: list[str],
                 initial_state: str,
                 alphabet: list[str],
                 table:dict[str, dict[str, str]],
                 table_reactions:dict[str, str]) -> None:
        super().__init__(states, initial_state, alphabet)
        self.table = table
        self.table_reactions = table_reactions

    def step(self, inp: str) -> None:
        """Machine step"""
        self.state = self.table[self.state][inp]

    def get_reaction(self):
        """Return reaction"""
        return self.table_reactions[self.state]
