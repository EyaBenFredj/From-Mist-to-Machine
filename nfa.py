class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  # {(state, symbol): [list of next states]}
        self.start_state = start_state
        self.accept_states = accept_states

    def epsilon_closure(self, state):
        """ Return the epsilon closure for a given state """
        closure = set([state])
        stack = [state]
        while stack:
            current = stack.pop()
            for next_state in self.transitions.get((current, 'ε'), []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure