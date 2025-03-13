"""Modules"""
from mealy_automata import MealyAutomata
from moor_automata import MoorAutomata
from transformation import mealy_to_moor
from pi_minimization import pi_minimization
from to_jflap_mealy import convert_mealy_to_jflap
from to_jflap_moor import convert_moor_to_jflap

def main():
    """Main function"""
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

    automata_minim = pi_minimization(automata)
    print("Результат работы над строчкой 'abba' нормализованного автомата Мили "+"".join([automata_minim.step(i) for i in "abba"]))

    res = ""
    moor = mealy_to_moor(automata)
    for i in "abba":
        moor.step(i)
        res += moor.get_reaction()
    print(f"Результат работы над строчкой 'abba' автомата Мура {res}")

    convert_moor_to_jflap(moor, "test_moor")
    convert_mealy_to_jflap(automata_minim, "test_mealy")

if __name__ == "__main__":
    main()
