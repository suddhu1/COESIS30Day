import networkx as nx
import matplotlib.pyplot as plt

def draw_nfa_dfa(transitions, start_state, accept_states, title):
    G = nx.DiGraph()
    
    # Add edges based on transitions
    for (src, symbol), dest in transitions.items():
        if isinstance(dest, set):  # For DFA, multiple destinations can merge
            dest = ','.join(dest)
        G.add_edge(src, dest, label=symbol)

    pos = nx.spring_layout(G, seed=42)  # Set layout
    labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}

    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=12, edge_color="black")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
    
    # Highlight start and accept states
    nx.draw_networkx_nodes(G, pos, nodelist=[start_state], node_color="green", node_size=2000)  # Start state
    nx.draw_networkx_nodes(G, pos, nodelist=accept_states, node_color="red", node_size=2000)  # Accept states

    plt.title(title)
    plt.show()

# Define NFA for the first grammar P1: σ → aA, σ → aσ, A → bA, A → λ
nfa_transitions = {
    ('σ', 'a'): {'A', 'σ'},
    ('A', 'b'): {'A'}
}
start_state_nfa = 'σ'
accept_states_nfa = {'A'}

# Define DFA transitions after subset construction
dfa_transitions = {
    ('σ', 'a'): {'A', 'σ'},
    ('A,σ', 'a'): {'A,σ'},
    ('A,σ', 'b'): {'A'},
    ('A', 'b'): {'A'}
}
start_state_dfa = 'σ'
accept_states_dfa = {'A', 'A,σ'}

# Draw NFA
draw_nfa_dfa(nfa_transitions, start_state_nfa, accept_states_nfa, "NFA for P1")

# Draw DFA
draw_nfa_dfa(dfa_transitions, start_state_dfa, accept_states_dfa, "DFA for P1")
