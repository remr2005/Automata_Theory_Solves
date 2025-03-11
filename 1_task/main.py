"""Modules"""
from mealy_automata import MealyAutomata
from moor_automata import MoorAutomata

def main():
    """Main function"""
    # Список состояний
    states = ["q0", "q1", "q2"]
    # Начальное состояние
    initial_state = "q0"
    # Алфавит
    alphabet = ["a", "b"]
    # Таблица переходов и реакций
    table = {
        "q0": {"a": ["q1", "y"], "b": ["q2", "x"]},
        "q1": {"a": ["q2", "z"], "b": ["q0", "w"]},
        "q2": {"a": ["q0", "t"], "b": ["q1", "v"]}
    }

    # Создаем объект автомата
    mealy = MealyAutomata(states, initial_state, alphabet, table)
    print(mealy.step("a"))
    table = {
        "q0": {"a": "q1", "b": "q2"},
        "q1": {"a": "q2", "b": "q0"},
        "q2": {"a": "q0", "b": "q1"}
    }
    # Таблица реакций
    table_reactions = {
        "q0": "Reaction 0",
        "q1": "Reaction 1",
        "q2": "Reaction 2"
    }
    moor = MoorAutomata(states, initial_state,alphabet,table,table_reactions)
    moor.step("a")
    print(moor.get_reaction())

if __name__ == "__main__":
    main()
