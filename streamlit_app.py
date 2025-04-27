import warnings
warnings.filterwarnings("ignore")  # Désactive tous les warnings Python

import streamlit as st
import os
from PIL import Image
from nfa import NFA
from dfa import DFA
from visualize import draw_automaton

# Titre et description
st.title("🚀 Générateur d'Automates : ε-NFA vers DFA")
st.write("""
Entrez les transitions de votre automate, et nous générerons :
- Le graphe de l'ε-NFA
- Le graphe du DFA correspondant
- Tester si une chaîne est **acceptée** par le DFA !
""")

# Barre latérale pour les entrées
st.sidebar.header("⚙️ Construisez votre Automate")

# États et alphabet
states_input = st.sidebar.text_input("États (séparés par des virgules)", "Q0,Q1,Q2,1,2")
alphabet_input = st.sidebar.text_input("Alphabet (séparé par des virgules)", "a,b")

# État initial et états finaux
start_state_input = st.sidebar.text_input("État initial", "Q0")
accept_states_input = st.sidebar.text_input("États finaux (séparés par des virgules)", "1,2")

# Zones de saisie pour les transitions
transitions_input = st.sidebar.text_area(
    "Transitions (une par ligne : état,symbole->état)",
    value="Q0,a->1\nQ0,a->Q1\nQ1,a->Q\nQ1,b->Q\nQ2,b->2\nQ,b->Q\nQ,a->Q"
)

# Bouton pour réinitialiser tous les champs
if st.sidebar.button("🧹 Réinitialiser les champs"):
    st.experimental_rerun()

# Bouton pour construire les automates
if st.sidebar.button("Construire l'Automate"):
    with st.spinner("Construction de l'automate en cours..."):
        # Analyse des entrées
        states = set(states_input.strip().split(','))
        alphabet = set(alphabet_input.strip().split(','))
        accept_states = set(accept_states_input.strip().split(','))

        transitions = {}
        for line in transitions_input.strip().split('\n'):
            parts = line.split('->')
            if len(parts) != 2:
                st.error(f"Format de transition invalide : {line}")
                st.stop()

            part1, part2 = parts
            if ',' not in part1:
                st.error(f"Format de transition invalide : {line}")
                st.stop()

            src, symbol = part1.split(',')
            dest = part2
            transitions.setdefault((src.strip(), symbol.strip()), []).append(dest.strip())

        # Création de l'NFA
        nfa = NFA(states, alphabet.union({'ε'}), transitions, start_state_input.strip(), accept_states)

        # Dessiner l'NFA
        nfa_image_path = draw_automaton(
            nfa.transitions,
            nfa.states,
            nfa.start_state,
            nfa.accept_states,
            filename="outputs/nfa_graph"
        )

        # Afficher l'NFA avec téléchargement
        if os.path.exists(nfa_image_path):
            st.subheader("🌫️ ε-NFA généré")
            nfa_image = Image.open(nfa_image_path)
            st.image(nfa_image, caption="Graphe de l'ε-NFA", use_container_width=True)

            with open(nfa_image_path, "rb") as file:
                st.download_button(
                    label="📥 Télécharger le graphe de l'ε-NFA",
                    data=file,
                    file_name="nfa_graph.png",
                    mime="image/png"
                )
        else:
            st.error("❌ Impossible de trouver le graphe de l'ε-NFA.")

        # Création du DFA
        dfa = DFA()
        dfa.from_nfa(nfa)

        # Dessiner le DFA
        dfa_image_path = draw_automaton(
            dfa.transitions,
            dfa.states,
            dfa.start_state,
            dfa.accept_states,
            filename="outputs/dfa_graph"
        )

        # Afficher le DFA avec téléchargement
        if os.path.exists(dfa_image_path):
            st.subheader("✅ DFA généré")
            dfa_image = Image.open(dfa_image_path)
            dfa_image = dfa_image.resize((600, int(600 * dfa_image.height / dfa_image.width)))
            st.image(dfa_image, caption="Graphe du DFA")

            with open(dfa_image_path, "rb") as file:
                st.download_button(
                    label="📥 Télécharger le graphe du DFA",
                    data=file,
                    file_name="dfa_graph.png",
                    mime="image/png"
                )
        else:
            st.error("❌ Impossible de trouver le graphe du DFA.")

        # Sauvegarder le DFA dans la session pour tester les chaînes
        st.session_state['dfa'] = dfa

    st.success("Automates générés avec succès ! 🎉")

# Section pour tester des chaînes sur le DFA
st.header("🧪 Tester une chaîne sur votre DFA")

if 'dfa' in st.session_state:
    test_string = st.text_input("Entrez une chaîne à tester", "")


    if st.button("Tester la chaîne"):
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
            st.success(f"✅ La chaîne '{test_string}' est ACCEPTÉE !")
        else:
            st.error(f"❌ La chaîne '{test_string}' est REJETÉE.")
else:
    st.warning("⚠️ Veuillez d'abord construire un automate pour tester une chaîne.")
