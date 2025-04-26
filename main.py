from nfa import NFA
from dfa import DFA
from visualize import draw_automaton

def main():
    # Exemple de création manuelle d'un NFA simple
    states = {'A', 'B', 'C'}
    alphabet = {'a', 'b', 'ε'}
    transitions = {
        ('A', 'ε'): ['B'],
        ('B', 'a'): ['B', 'C'],
        ('C', 'b'): ['C']
    }
    start_state = 'A'
    accept_states = {'C'}

    nfa = NFA(states, alphabet, transitions, start_state, accept_states)

    # Visualiser le NFA
    draw_automaton(nfa.transitions, nfa.states, nfa.start_state, nfa.accept_states, "nfa")

    # Déterminiser le NFA -> DFA
    dfa = DFA()
    dfa.from_nfa(nfa)

    # Visualiser le DFA
    draw_automaton(dfa.transitions, dfa.states, dfa.start_state, dfa.accept_states, "dfa")

if __name__ == "__main__":
    main()