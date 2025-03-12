import xml.etree.ElementTree as ET

def convert_to_jflap(table, start_state, filename="mealy_machine.jff"):
    structure = ET.Element("structure")
    etype = ET.SubElement(structure, "type")
    etype.text = "mealy"
    automaton = ET.SubElement(structure, "automaton")
    
    # Создание состояний
    states = {}
    for state in table.keys():
        state_elem = ET.SubElement(automaton, "state", id=state, name=state)
        if state == start_state:
            ET.SubElement(state_elem, "initial")
        states[state] = state_elem
    
    # Создание переходов
    for from_state, transitions in table.items():
        for symbol, (to_state, output) in transitions.items():
            transition = ET.SubElement(automaton, "transition")
            ET.SubElement(transition, "from").text = from_state
            ET.SubElement(transition, "to").text = to_state
            ET.SubElement(transition, "read").text = symbol
            ET.SubElement(transition, "transout").text = output
    
    tree = ET.ElementTree(structure)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"Файл {filename} создан!")

# Таблица состояний
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

# Начальное состояние
start_state = "1"

# Запуск конвертации
convert_to_jflap(table, start_state)

table_norm = {
    "1":{"a":["1","x"],"b":["9","y"]},
    "9":{"a":["2","y"], "b":["1","x"]},
    "3":{"a":["9","x"],"b":["9","x"]},
    "2":{"a":["3","y"], "b":["1","y"]},
    "6":{"a":["9","x"], "b":["9","y"]}
}

convert_to_jflap(table_norm, "1", "mealy_norm.jff")