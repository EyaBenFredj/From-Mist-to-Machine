class DFA:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.transitions = {}
        self.start_state = None
        self.accept_states = []

    def from_nfa(self, nfa):
        """ Build DFA from NFA using subset construction """
        initial_closure = frozenset(nfa.epsilon_closure(nfa.start_state))
        unmarked_states = [initial_closure]
        dfa_states = {initial_closure: 'Q0'}
        self.start_state = 'Q0'
        state_counter = 1

        while unmarked_states:
            current = unmarked_states.pop()
            for symbol in nfa.alphabet:
                if symbol == 'ε':
                    continue
                next_states = set()
                for nfa_state in current:
                    for target in nfa.transitions.get((nfa_state, symbol), []):
                        next_states.update(nfa.epsilon_closure(target))
                if not next_states:
                    continue
                next_states_frozen = frozenset(next_states)
                if next_states_frozen not in dfa_states:
                    dfa_states[next_states_frozen] = f"Q{state_counter}"
                    state_counter += 1
                    unmarked_states.append(next_states_frozen)
                self.transitions[(dfa_states[current], symbol)] = dfa_states[next_states_frozen]

        self.states = list(dfa_states.values())
        self.accept_states = [
            name for states_set, name in dfa_states.items()
            if any(s in nfa.accept_states for s in states_set)
        ]