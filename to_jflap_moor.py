import xml.etree.ElementTree as ET

def convert_to_jflap(states, transitions, initial_state):
    root = ET.Element("structure")
    ET.SubElement(root, "type").text = "moore"
    automaton = ET.SubElement(root, "automaton")
    
    state_map = {state: str(i) for i, state in enumerate(states.keys())}
    
    for state, output in states.items():
        state_elem = ET.SubElement(automaton, "state", id=state_map[state], name=state)
        # ET.SubElement(state_elem, "x").text = str(100 + int(state[1]) * 50)
        # ET.SubElement(state_elem, "y").text = str(100 + int(state[1]) * 50)
        ET.SubElement(state_elem, "output").text = output
        if state == initial_state:
            ET.SubElement(state_elem, "initial")
    
    for from_state, paths in transitions.items():
        for symbol, to_state in paths.items():
            trans_elem = ET.SubElement(automaton, "transition")
            ET.SubElement(trans_elem, "from").text = state_map[from_state]
            ET.SubElement(trans_elem, "to").text = state_map[to_state]
            ET.SubElement(trans_elem, "read").text = symbol
            ET.SubElement(trans_elem, "transout").text = states[to_state]
    
    tree = ET.ElementTree(root)
    tree.write("automaton.jff", encoding="utf-8", xml_declaration=True)

states = {
    "A0": "x", "A1": "y", "A2": "y", "A3": "x", "A4": "y", "A5": "y", "A6": "-"
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

convert_to_jflap(states, transitions, initial_state)