"""Modules"""
from moor_automata import MoorAutomata
from mealy_automata import MealyAutomata
from collections import defaultdict

def mealy_to_moor(automata: MealyAutomata):
    """Transform Mealy automata to Moor automata"""
    mealy_to_moor_states = defaultdict()
    dt = defaultdict(set)
    for s in automata.states:
        for a in automata.alphabet:
            n_s, r = automata.table[s][a]
            dt[n_s].add(r)
    i = 0
    new_states_to_old_states = dict()
    new_states = dict()
    for s in automata.states:
        for _ in dt[s]:
            new_states_to_old_states[f"A{i}"] = s
            i+=1
        if len(dt[s]) == 0:
            new_states_to_old_states[f"A{i}"] = s
        i+=1

    print(new_states_to_old_states)

