from dfa import DFA

# Create a simple DFA manually
dfa = DFA()
dfa.states = {'q0', 'q1'}
dfa.start_state = 'q0'
dfa.accept_states = {'q1'}
dfa.alphabet = {'a', 'b'}
dfa.transitions = {
    ('q0', 'a'): 'q1',
    ('q1', 'b'): 'q0'
}

def test_dfa(dfa, input_string):
    current_state = dfa.start_state
    for symbol in input_string:
        key = (current_state, symbol)
        if key in dfa.transitions:
            current_state = dfa.transitions[key]
        else:
            return False
    return current_state in dfa.accept_states

string = input("Enter a string to test: ")
if test_dfa(dfa, string):
    print("✅ String accepted!")
else:
    print("❌ String rejected.")