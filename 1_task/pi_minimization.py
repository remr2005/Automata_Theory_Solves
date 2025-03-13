"""Modules"""
from collections import defaultdict
from copy import deepcopy
from mealy_automata import MealyAutomata
from moor_automata import MoorAutomata
from transformation import mealy_to_moor

def pi_minimization(automata_: MealyAutomata):
    """Pi-minimization"""
    automata = deepcopy(automata_)
    # Находим таблицу реакций и переходов, а так же все уникальные столбцы реакций
    table_trans = {s:{a_n:i[0] for a_n, i in a.items()} for s,a in automata.table.items()}
    table_react = {s:{a_n:i[1] for a_n, i in a.items()} for s,a in automata.table.items()}
    unikal_reactions = list(set(tuple(j for _,j in a.items()) for _, a in table_react.items()))
    
    # Разделяем состояния по реакциям
    reactions = defaultdict(dict)
    reactions_ = {}
    for s, a in deepcopy(table_react).items():
        try:
            ind = unikal_reactions.index(tuple(react for _,react in a.items()))
            reactions[ind][s] = a
            reactions_[s] = ind
        except:
            continue

    # Начнем расщепление и минимизацию
    ind_char = 65
    while True:
        temp_reactions = defaultdict(dict)
        temp_reactions_ = {}
        for _, group in reactions.items():
            # Теперь разделяем по переходам
            for s, a in group.items():
                for inp in a:
                    group[s][inp] = reactions_[table_trans[s][inp]]
            unikal_reactions = list(set(tuple(j for _,j in a.items()) for _, a in group.items()))

            for s, a in group.items():
                try:
                    ind = unikal_reactions.index(tuple(react for _,react in a.items()))
                    temp_reactions[f"{chr(ind_char)}{ind}"][s] = a
                    temp_reactions_[s] = f"{chr(ind_char)}{ind}"
                except:
                    continue
            ind_char+=1
        if len(temp_reactions.keys()) == len(reactions.keys()):
            break
        reactions = temp_reactions
        reactions_ = temp_reactions_ 
    
    # Возвращаем первоночальные состояния и убираем эквивалентые
    dt = {}
    dt_ = {}
    for s, a in reactions.items():
        k = list(a.keys())[0]
        dt[k] =  a[k]
        dt_[s] = k
    for s,a in dt.items():
        for inp,tran in a.items():
            dt[s][inp] = [dt_[tran],table_react[s][inp]]
    automata.states = list(dt.keys())
    automata.state = automata.states[0]
    automata.table = dt
    return automata
