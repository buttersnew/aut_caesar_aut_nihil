import os
import sys
from pyvis.network import Network

# Import shared loader from the same directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_companion_stable_groups import load_companion_data

# Load data directly from module_troops.py and module_scripts.py
companions, conflicts, cultures, likes = load_companion_data()


# Initialize Network
net = Network(height='900px', width='100%', bgcolor='#222222', font_color='white')

# --- PASS 1: Create Nodes ---
for name in companions:
    culture = cultures.get(name, 'Unknown')

    # Tooltip content
    tooltip_text = f"{name}\n------------------\nCulture: {culture}"

    # Color Logic
    color = '#3b82f6'                               # Default: Medium Blue
    if 'Roman' in culture:      color = '#8e44ad'   # Roman: Rich Purple
    elif 'Parthian' in culture: color = '#d35400'   # Parthian: Burnt Orange
    elif culture in ('Germanic', 'Britonic'): color = '#27ae60'  # Barbarian: Forest Green
    elif 'Egyptian' in culture: color = '#f1c40f'   # Egyptian: Gold
    elif 'Judean' in culture:   color = '#3498db'   # Judean: Dark Cyan
    elif 'Sarmatian' in culture: color = '#c0392b'  # Sarmatian: Deep Red
    elif 'Berber' in culture:   color = '#e67e22'   # Berber: Orange
    elif 'Saka' in culture:     color = '#1abc9c'   # Saka: Teal

    net.add_node(
        name,
        label=name,
        title=tooltip_text,
        color=color,
        shape='box',
        borderWidth=1,
        font={
            'size': 40,
            'color': 'white',
            'strokeWidth': 4,
            'strokeColor': 'black'
        }
    )

# --- PASS 2: Create Relationships ---
node_ids = {n['id'] for n in net.nodes}

for name, liked_name in likes.items():
    if name in node_ids and liked_name in node_ids:
        net.add_edge(name, liked_name, color='#66ff66', width=3, title="Likes")

for name, hated_list in conflicts.items():
    for hated_name in hated_list:
        if name in node_ids and hated_name in node_ids:
            net.add_edge(name, hated_name, color='#ff6666', width=1, dashes=True, title="Hates")

# Settings
net.barnes_hut(gravity=-3000, central_gravity=0.3, spring_length=200, spring_strength=0.05, damping=0.09)
# net.show_buttons(filter_=['physics'])
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'website', 'content', 'companion_graph.html')
net.show(output_path, notebook=False)