"""Modules"""
from collections import defaultdict
from moor_automata import MoorAutomata
from mealy_automata import MealyAutomata

def mealy_to_moor(automata: MealyAutomata):
    """Transform Mealy automata to Moor automata"""
    dt = defaultdict(set)
    for s in automata.states:
        for a in automata.alphabet:
            n_s, r = automata.table[s][a]
            dt[n_s].add(r)
    i = 0
    new_states_to_old_states = dict()
    new_states = dict()
    old_state_to_new_state = dict()
    table_reaction = dict()
    for s in automata.states:
        for r in dt[s]:
            old_state_to_new_state[s] = f"A{i}"
            new_states_to_old_states[f"A{i}"] = s
            new_states[(s, r)] = f"A{i}"
            table_reaction[f"A{i}"] = r
            i+=1
        if len(dt[s]) == 0:
            old_state_to_new_state[s] = f"A{i}"
            new_states_to_old_states[f"A{i}"] = s
            new_states[(s, "")] = f"A{i}"
            table_reaction[f"A{i}"] = ""
            i+=1
    table = defaultdict(dict)
    for s in new_states_to_old_states:
        for i in automata.alphabet:
            old_state = new_states_to_old_states[s]
            old_state1, r = automata.table[old_state][i]
            table[s][i] = new_states[(old_state1,r)]
    return MoorAutomata(table.keys(),
                         old_state_to_new_state[automata.state],
                         automata.alphabet,
                         table,
                         table_reaction)
