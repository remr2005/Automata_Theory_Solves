"""Modules"""
from copy import deepcopy
from collections import defaultdict
from mealy_automata import MealyAutomata
from moor_automata import MoorAutomata

def from_mealy_to_moor(automata: MealyAutomata):
    """Transform Mealy automata to Moor automata"""
    aut = deepcopy(automata)
    unikals = set()
    for _, a in aut.table.items():
        for _, i in a.items():
            unikals.add(tuple(i))
    dt = {i:f"A{ind}" for ind,i in enumerate(unikals)}
    table_reactions = {f"A{ind}":i[1] for ind,i in enumerate(unikals)}
    table = defaultdict(dict)
    print(dt)
    for s1,i in dt.items():
        for s,a in aut.table.items():
            for inp, comb in a.items():
                table[i][inp] = dt[tuple(comb)]
    
    state_old = list(set(i[0] for _,i in enumerate(dt.keys())))
    ind = 0
    for s,i in aut.table.items():
        if s not in state_old:
            for inp,comb in i.items():
                table[f"B{ind}"][inp] = dt[tuple(comb)]
                table_reactions[f"B{ind}"] = ""
            ind +=1
    states = list(table.keys())
    return MoorAutomata(states,states[0],aut.alphabet,table,table_reactions)


table = {
        "1": {"a": ["4", "x"], "b": ["7", "y"]},
        "2": {"a": ["3", "y"], "b": ["4", "y"]},
        "3": {"a": ["7", "x"], "b": ["9", "x"]},
        "4": {"a": ["5", "x"], "b": ["9", "y"]},
        "5": {"a": ["8", "x"], "b": ["7", "y"]},
        "6": {"a": ["7", "x"], "b": ["9", "y"]},
        "7": {"a": ["2", "y"], "b": ["8", "x"]},
        "8": {"a": ["5", "x"], "b": ["9", "y"]},
        "9": {"a": ["2", "y"], "b": ["5", "x"]}
    }

string = "abbabba"
    # Список состояний
states = list(table.keys())

    # Начальное состояние
initial_state = "8"

    # Алфавит входных символов
alphabet = ["a", "b"]

automata = MealyAutomata(states, initial_state, alphabet, table)
from_mealy_to_moor(automata)