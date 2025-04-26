import streamlit as st
import os

from nfa import NFA
from dfa import DFA
from visualize import draw_automaton

# Title and description
st.title("🚀 Automata Generator: ε-NFA to DFA")
st.write("""
Enter your automaton transitions, and we'll generate:
- The ε-NFA graph
- The corresponding DFA graph
- Test if a string is **accepted** by the DFA!
""")

# Sidebar for inputs
st.sidebar.header("⚙️ Build your Automaton")

# States and alphabet
states_input = st.sidebar.text_input("States (comma-separated)", "Q0,Q1,Q2,1,2")
alphabet_input = st.sidebar.text_input("Alphabet (comma-separated)", "a,b")

# Start and accepting states
start_state_input = st.sidebar.text_input("Start state", "Q0")
accept_states_input = st.sidebar.text_input("Accepting states (comma-separated)", "1,2")

# Transitions input area
transitions_input = st.sidebar.text_area(
    "Transitions (one per line: state,symbol->state)",
    value="Q0,a->1\nQ0,a->Q1\nQ1,a->Q\nQ1,b->Q\nQ2,b->2\nQ->b->Q\nQ->a->Q"
)

# Button to build automata
if st.sidebar.button("Build Automata"):
    with st.spinner("Building Automata..."):
        # Parse inputs
        states = set(states_input.strip().split(','))
        alphabet = set(alphabet_input.strip().split(','))
        accept_states = set(accept_states_input.strip().split(','))

        transitions = {}
        for line in transitions_input.strip().split('\n'):
            if '->' in line:
                part1, part2 = line.split('->')
                src, symbol = part1.split(',')
                dest = part2
                transitions.setdefault((src.strip(), symbol.strip()), []).append(dest.strip())

        # Create NFA
        nfa = NFA(states, alphabet.union({'ε'}), transitions, start_state_input.strip(), accept_states)

        # Draw NFA
        nfa_image_path = draw_automaton(
            nfa.transitions,
            nfa.states,
            nfa.start_state,
            nfa.accept_states,
            filename="outputs/nfa_graph"
        )

        # Display NFA
        if os.path.exists(nfa_image_path):
            st.subheader("🌫️ ε-NFA")
            st.image(nfa_image_path, caption="Generated ε-NFA", use_column_width=True)
        else:
            st.error("❌ NFA graph not found!")

        # Create DFA from NFA
        dfa = DFA()
        dfa.from_nfa(nfa)

        # Draw DFA
        dfa_image_path = draw_automaton(
            dfa.transitions,
            dfa.states,
            dfa.start_state,
            dfa.accept_states,
            filename="outputs/dfa_graph"
        )

        # Display DFA
        if os.path.exists(dfa_image_path):
            st.subheader("✅ DFA")
            st.image(dfa_image_path, caption="Generated DFA", use_column_width=True)
        else:
            st.error("❌ DFA graph not found!")

        # Save DFA for string testing in session state
        st.session_state['dfa'] = dfa

    st.success("Automata generated successfully! 🎉")

# Section to test strings on DFA
st.header("🧪 Test a String on your DFA")

if 'dfa' in st.session_state:
    test_string = st.text_input("Enter a string to test", "")

    if st.button("Test String"):
        def test_dfa(dfa, input_string):
            current_state = dfa.start_state
            for symbol in input_string:
                key = (current_state, symbol)
                if key in dfa.transitions:
                    current_state = dfa.transitions[key]
                else:
                    return False
            return current_state in dfa.accept_states

        result = test_dfa(st.session_state['dfa'], test_string)

        if result:
            st.success(f"✅ The string '{test_string}' is ACCEPTED!")
        else:
            st.error(f"❌ The string '{test_string}' is REJECTED.")
else:
    st.warning("⚠️ Please build an automaton first to enable string testing.")
