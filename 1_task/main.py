"""Modules"""
from mealy_automata import MealyAutomata
from moor_automata import MoorAutomata
from transformation import mealy_to_moor

def main():
    """Main function"""
    # Список состояний
    states = ["q0", "q1", "q2"]
    # Начальное состояние
    initial_state = "q0"
    # Алфавит
    alphabet = ["x1", "x2"]
    # Таблица переходов и реакций
    table = {
        "q0": {"x1": ["q2", "y1"], "x2": ["q1", "y1"]},
        "q1": {"x1": ["q1", "y1"], "x2": ["q2", "y2"]},
        "q2": {"x1": ["q1", "y2"], "x2": ["q1", "y1"]}
    }

    # Создаем объект автомата
    mealy = MealyAutomata(states, initial_state, alphabet, table)
    moor = mealy_to_moor(mealy)
    print(moor.table)
    print(moor.table_reactions)

if __name__ == "__main__":
    main()
