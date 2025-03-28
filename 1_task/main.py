"""Modules"""
from mealy_automata import MealyAutomata
from moor_automata import MoorAutomata
from transformation import mealy_to_moor
from pi_minimization import pi_minimization
from to_jflap_mealy import convert_mealy_to_jflap
from to_jflap_moor import convert_moor_to_jflap
from transformation2 import from_mealy_to_moor

def main():
    """Main function"""
    table = {
        "1": {"a": ["2", "y"], "b": ["3", "y"]},
        "2": {"a": ["1", "y"], "b": ["3", "y"]},
        "3": {"a": ["6", "y"], "b": ["2", "x"]},
        "4": {"a": ["4", "y"], "b": ["6", "y"]},
        "5": {"a": ["7", "y"], "b": ["5", "y"]},
        "6": {"a": ["3", "y"], "b": ["4", "x"]},
        "7": {"a": ["7", "x"], "b": ["8", "x"]},
        "8": {"a": ["7", "y"], "b": ["9", "y"]},
        "9": {"a": ["7", "y"], "b": ["8", "y"]}
        # "1": {"a": ["2", "x"], "b": ["4", "x"]},
        # "2": {"a": ["1", "x"], "b": ["4", "x"]},
        # "3": {"a": ["4", "x"], "b": ["2", "y"]},
        # "4": {"a": ["4", "x"], "b": ["4", "x"]},
        # "5": {"a": ["5", "x"], "b": ["6", "x"]},
        # "6": {"a": ["7", "x"], "b": ["6", "x"]},
        # "7": {"a": ["6", "x"], "b": ["6", "x"]},
        # "8": {"a": ["7", "x"], "b": ["5", "y"]},
        # "9": {"a": ["9", "y"], "b": ["8", "y"]}
    }

    string = "abba"
    # Список состояний
    states = list(table.keys())

    # Начальное состояние
    initial_state = "1"

    # Алфавит входных символов
    alphabet = ["a", "b"]

    automata = MealyAutomata(states, initial_state, alphabet, table)
    print("Результат работы над строчкой 'abba' автомата Мили "+"".join([automata.step(i) for i in string]))

    automata_minim = pi_minimization(automata)
    print(automata_minim.table)
    automata_minim.state = "1"
    print("Результат работы над строчкой 'abba' нормализованного автомата Мили "+"".join([automata_minim.step(i) for i in string]))

    res = ""
    moor = mealy_to_moor(automata_minim)
    print(moor.table_reactions)
    for i in string:
        moor.step(i)
        res += moor.get_reaction()
    print(f"Результат работы над строчкой 'abba' автомата Мура {res}")

    convert_moor_to_jflap(moor, "test_moor")
    convert_mealy_to_jflap(automata_minim, "test_mealy")

if __name__ == "__main__":
    main()
