from graphviz import Digraph

def draw_automaton(transitions, states, start_state, accept_states, filename, rankdir="LR"):
    dot = Digraph()
    dot.attr(rankdir=rankdir)

    for state in states:
        if state in accept_states:
            dot.node(state, shape='doublecircle', style='filled', color='lightgrey')
        else:
            dot.node(state, shape='circle')

    dot.node('', shape='none')
    dot.edge('', start_state)

    for (src, symbol), dest_list in transitions.items():
        for dest in dest_list:
            if symbol == 'ε':
                dot.edge(src, dest, label=symbol, color="red", fontcolor="red")
            else:
                dot.edge(src, dest, label=symbol)

    output_path = dot.render(filename=filename, format="png", cleanup=True)
    return output_path  # <--- important: return the real path