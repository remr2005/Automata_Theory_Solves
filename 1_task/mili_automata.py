"""Import base modules"""
from base_automata import BaseAutomata

class MiliAutomata(BaseAutomata):
    """Realisation of Mili Automata"""
    def __init__(self, states: list[str],
                 initial_state: str,
                 alphabet: list[str],
                 table:dict[str, list]) -> None:
        super().__init__(states, initial_state, alphabet)
        self.table = table
