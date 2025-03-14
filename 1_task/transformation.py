"""Modules"""
from collections import defaultdict
from copy import deepcopy
from moor_automata import MoorAutomata
from mealy_automata import MealyAutomata

def mealy_to_moor(automata_: MealyAutomata) -> MoorAutomata:
    """Transforms a Mealy automaton into a Moore automaton."""
    automata = deepcopy(automata_)
    state_reactions = defaultdict(set)
    for state in automata.states:
        for symbol in automata.alphabet:
            next_state, reaction = automata.table[state][symbol]
            state_reactions[next_state].add(reaction)

    new_states = {}
    reaction_table = {}
    old_to_new_state = {}
    state_counter = 0

    for state in automata.states:
        if not state_reactions[state]:
            state_reactions[state].add("")  # Для состояния без реакций

        for reaction in state_reactions[state]:
            new_state = f"A{state_counter}"
            new_states[(state, reaction)] = new_state
            reaction_table[new_state] = reaction
            old_to_new_state[state] = new_state
            state_counter += 1

    transition_table = defaultdict(dict)
    for new_state, old_state in new_states.items():
        for symbol in automata.alphabet:
            next_old_state, reaction = automata.table[new_state[0]][symbol]
            transition_table[old_state][symbol] = new_states[(next_old_state, reaction)]

    return MoorAutomata(
        states=list(transition_table.keys()),
        initial_state=old_to_new_state[automata.state],
        alphabet=automata.alphabet,
        table=transition_table,
        table_reactions=reaction_table
    )
