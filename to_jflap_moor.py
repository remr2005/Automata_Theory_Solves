import xml.etree.ElementTree as ET

def create_jflap_moore(states, transitions, initial_state, filename="moore_machine.jff"):
    root = ET.Element("structure")
    ET.SubElement(root, "type").text = "moore"
    automaton = ET.SubElement(root, "automaton")
    
    state_elements = {}
    for i, (state, output) in enumerate(states.items()):
        state_el = ET.SubElement(automaton, "state", id=str(i), name=state)
        if state == initial_state:
            ET.SubElement(state_el, "initial")
        ET.SubElement(state_el, "output").text = output  # Добавляем выходной символ (реакцию)
        state_elements[state] = i
    
    for state, trans in transitions.items():
        for input_symbol, next_state in trans.items():
            transition = ET.SubElement(automaton, "transition")
            ET.SubElement(transition, "from").text = str(state_elements[state])
            ET.SubElement(transition, "to").text = str(state_elements[next_state])
            ET.SubElement(transition, "read").text = input_symbol
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def main():
    states = {
        "A0": "x", "A1": "y", "A2": "y", "A3": "x", "A4": "y", "A5": "y", "A6": "y"
    }
    transitions = {
        "A0": {"a": "A0", "b": "A2"},
        "A1": {"a": "A0", "b": "A2"},
        "A2": {"a": "A5", "b": "A0"},
        "A3": {"a": "A5", "b": "A0"},
        "A4": {"a": "A3", "b": "A3"},
        "A5": {"a": "A4", "b": "A1"},
        "A6": {"a": "A3", "b": "A2"}
    }
    initial_state = "A0"
    create_jflap_moore(states, transitions, initial_state, "moore_machine.jff")

if __name__ == "__main__":
    main()
