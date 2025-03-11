from mealy_automata import MealyAutomata
from collections import defaultdict
from moor_automata import MoorAutomata
from transformation import mealy_to_moor

def minimization(automata: MealyAutomata):
    reactions = {}
    ind = 1
    table = automata.table
    old_states_to_new = {}
    for s, i in table.items():
        reaction = tuple(i[a][1] for a in automata.alphabet)
        if reaction not in reactions:
            # print(s, reaction)
            reactions[reaction] = f"A{ind}"
            ind+=1
    for s, i in table.items():
        reaction = tuple(i[a][1] for a in automata.alphabet)
        old_states_to_new[s] = reactions[reaction]

    table1= defaultdict(dict)
    for s, i in table.items():
        for a in automata.alphabet:
            table1[s][a] = old_states_to_new[table[s][a][0]]
    
    table2 = defaultdict(dict)
    ind2 = 66
    while True:
        old_states_to_new1 = {}
        reactions1 ={}
        ind = 1
        for s, i in table1.items():
            reaction1 = tuple(j for _,j in i.items())
            if reaction1 not in reactions1:
                # print(s, reaction1)
                reactions1[reaction1] = f"{chr(ind2)}{ind}"
                ind+=1
        for s, i in table1.items():
            reaction1 = tuple(j for _,j in i.items())
            old_states_to_new1[s] = reactions1[reaction1]
        for s, i in table.items():
            for a in alphabet:
                table1[s][a] = old_states_to_new1[table[s][a][0]]
        ind2+=1       
        if table1 == table2:
            break
        table2 = table1
    new_to_old = {j:i for i,j in old_states_to_new1.items()}
    table2= defaultdict(dict)
    for s, i in table.items():
        for a in alphabet:
            table2[old_states_to_new1[s]][a] = (table1[s][a], table[s][a][1])
    table3 =defaultdict(dict)
    for s,i in table2.items():
        for a in alphabet:
            table3[new_to_old[s]][a] = (new_to_old[table2[s][a][0]], table2[s][a][1])
    return table3













# Таблица переходов и реакций для автомата Мили
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


# Список состояний
states = list(table.keys())

# Начальное состояние
initial_state = "8"

# Алфавит входных символов
alphabet = ["a", "b"]

automata = MealyAutomata(states, initial_state, alphabet, table)
print("Результат работы над строчкой 'abba' автомата Мили "+"".join([automata.step(i) for i in "abba"]))

automata.table = minimization(automata)
automata.states = automata.table.keys()
automata.state = "8"
print("Результат работы над строчкой 'abba' нормализованного автомата Мили "+"".join([automata.step(i) for i in "abba"]))

res = ""
moor = mealy_to_moor(automata)
for i in "abba":
    moor.step(i)
    res += moor.get_reaction()
print(f"Результат работы над строчкой 'abba' автомата Мура {res}")