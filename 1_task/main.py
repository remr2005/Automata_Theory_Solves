"""Modules"""
from mili_automata import MiliAutomata
from mure_automata import MureAutomata

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
    automata = MiliAutomata(states, initial_state, alphabet, table)
    print(automata.step("a"))

if __name__ == "__main__":
    main()
