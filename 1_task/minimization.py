from mealy_automata import MealyAutomata
from collections import defaultdict

def minimization(automata: MealyAutomata):
    reactions = {}
    # Собираем уникальные реакции
    ind = 1
    table = automata.table
    old_states_to_new = {}
    for s, i in table.items():
        reaction = tuple(i[a][1] for a in automata.alphabet) # Используем tuple вместо list
        if reaction not in reactions:
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
    print(old_states_to_new1)
    print(table1)













# Таблица переходов и реакций для автомата Мили
table = {
    "1": {"a": ["7", "0"], "b": ["6", "1"], "c": ["1", "0"]},
    "2": {"a": ["7", "0"], "b": ["2", "1"], "c": ["1", "0"]},
    "3": {"a": ["8", "0"], "b": ["6", "1"], "c": ["3", "0"]},
    "4": {"a": ["8", "0"], "b": ["2", "1"], "c": ["3", "0"]},
    "5": {"a": ["7", "0"], "b": ["4", "1"], "c": ["3", "0"]},
    "6": {"a": ["5", "0"], "b": ["1", "1"], "c": ["1", "0"]},
    "7": {"a": ["1", "1"], "b": ["8", "0"], "c": ["3", "0"]},
    "8": {"a": ["3", "1"], "b": ["8", "0"], "c": ["1", "0"]}
}

# Список состояний
states = list(table.keys())

# Начальное состояние
initial_state = "1"

# Алфавит входных символов
alphabet = ["a", "b", "c"]

automata = MealyAutomata(states, initial_state, alphabet, table)
minimization(automata)