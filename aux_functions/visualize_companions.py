from pyvis.network import Network
import re

# Paste your text data here
data = """
<trp=686>Pravare Ytarim</> (Parthian): Likely in <p=27>Chersonesus</> (Streets).
     +) Likes <trp=687>Marius Gaius</>
     -) Hates <trp=692>Lavia</>
     -) Hates <trp=701>Titocuna</>
<trp=687>Marius Gaius</> (Roman): Likely in <p=42>Antiochia</> (Streets).
     +) Likes <trp=686>Pravare Ytarim</>
     -) Hates <trp=690>Satibarzanes</>
     -) Hates <trp=694>Aturius Spurus</>
<trp=688>Pulchra</> (Roman): Likely in <p=58>Nicomedia</> (Tavern).
     +) Likes <trp=694>Aturius Spurus</>
     -) Hates <trp=699>Titus</>
     -) Hates <trp=693>Hildr</>
<trp=689>Abadutiker</> (Germanic): Likely in <p=45>Tur</> (Streets).
     +) Likes <trp=690>Satibarzanes</>
     -) Hates <trp=695>Attaklos</>
     -) Hates <trp=692>Lavia</>
<trp=690>Satibarzanes</> (Parthian): Likely in <p=59>Ecbatana</> (Streets).
     +) Likes <trp=689>Abadutiker</>
     -) Hates <trp=687>Marius Gaius</>
     -) Hates <trp=696>Dionysia</>
<trp=691>Firentrix</> (Britonic): Likely in <p=50>Corduba</> (Tavern).
     +) Likes <trp=697>Jeremus</>
     -) Hates <trp=696>Dionysia</>
     -) Hates <trp=698>Chanakya</>
<trp=692>Lavia</> (Egyptian): Likely in <p=40>Alexandria</> (Streets).
     +) Likes <trp=701>Titocuna</>
     -) Hates <trp=686>Pravare Ytarim</>
     -) Hates <trp=689>Abadutiker</>
<trp=693>Hildr</> (Germanic): Likely in <p=65>Uburzis</> (Tavern).
     +) Likes <trp=698>Chanakya</>
     -) Hates <trp=697>Jeremus</>
     -) Hates <trp=688>Pulchra</>
<trp=694>Aturius Spurus</> (Roman): Likely in <p=32>Lugdunum</> (Tavern).
     +) Likes <trp=688>Pulchra</>
     -) Hates <trp=698>Chanakya</>
     -) Hates <trp=687>Marius Gaius</>
<trp=695>Attaklos</> (Roman): Likely in <p=57>Athenae</> (Tavern).
     +) Likes <trp=696>Dionysia</>
     -) Hates <trp=689>Abadutiker</>
     -) Hates <trp=699>Titus</>
<trp=696>Dionysia</> (Roman): Likely in <p=55>Thessalonica</> (Streets).
     +) Likes <trp=695>Attaklos</>
     -) Hates <trp=691>Firentrix</>
     -) Hates <trp=690>Satibarzanes</>
<trp=697>Jeremus</> (Roman): Likely in <p=22>Lutetia</> (Tavern).
     +) Likes <trp=691>Firentrix</>
     -) Hates <trp=693>Hildr</>
     -) Hates <trp=700>Artimenus</>
<trp=698>Chanakya</> (Sarmatian): Likely in <p=47>Ctesiphon</> (Streets).
     +) Likes <trp=693>Hildr</>
     -) Hates <trp=694>Aturius Spurus</>
     -) Hates <trp=691>Firentrix</>
<trp=699>Titus</> (Roman): Likely in <p=25>Mediolanum</> (Tavern).
     +) Likes <trp=700>Artimenus</>
     -) Hates <trp=688>Pulchra</>
     -) Hates <trp=695>Attaklos</>
<trp=700>Artimenus</> (Roman): Likely in <p=76>Vindobona</> (Hall).
     +) Likes <trp=699>Titus</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=697>Jeremus</>
<trp=701>Titocuna</> (Britonic): Likely in <p=21>Deva</> (Tavern).
     +) Likes <trp=692>Lavia</>
     -) Hates <trp=700>Artimenus</>
     -) Hates <trp=686>Pravare Ytarim</>
<trp=702>Anicetus</> (Roman): Likely in <p=34>Phasis</> (Tavern).
     +) Likes <trp=705>Secundus Minor</>
     -) Hates <trp=708>Lucius Varrus Drusus</>
<trp=703>Arminius Octavianus</> (Roman): Likely in <p=67>Palmyra</> (Streets).
     +) Likes <trp=704>Tertius Maior</>
     -) Hates <trp=722>Josephus</>
     -) Hates <trp=696>Dionysia</>
<trp=704>Tertius Maior</> (Roman): Likely in <p=67>Palmyra</> (Tavern).
     +) Likes <trp=725>Kara Boga</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=722>Josephus</>
<trp=705>Secundus Minor</> (Roman): Likely in <p=60>Dura Europos</> (Streets).
     +) Likes <trp=727>Chaditox</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=689>Abadutiker</>
<trp=706>Drusus</> (Roman): Likely in <p=56>Dyrrachium</> (Tavern).
     +) Likes <trp=707>Libertus Tiro</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=725>Kara Boga</>
<trp=707>Libertus Tiro</> (Roman): Likely in <p=52>Tarraco</> (Tavern).
     +) Likes <trp=701>Titocuna</>
     -) Hates <trp=708>Lucius Varrus Drusus</>
     -) Hates <trp=712>Lucullus Caepio</>
<trp=708>Lucius Varrus Drusus</> (Roman): Likely in <p=51>Augusta Emerita</> (Streets).
     +) Likes <trp=710>Sollius Modestus</>
     -) Hates <trp=707>Libertus Tiro</>
<trp=709>Sidonius Apollinaris</> (Roman): Likely in <p=39>Hierosolyma</> (Tavern).
     +) Likes <trp=710>Sollius Modestus</>
     -) Hates <trp=727>Chaditox</>
     -) Hates <trp=690>Satibarzanes</>
<trp=710>Sollius Modestus</> (Roman): Likely in <p=68>Thebae</> (Streets).
     +) Likes <trp=711>Albinus Basilius</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=698>Chanakya</>
<trp=711>Albinus Basilius</> (Roman): Likely in <p=70>Mtskheta</> (Tavern).
     +) Likes <trp=712>Lucullus Caepio</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=714>Fabianus</>
<trp=712>Lucullus Caepio</> (Roman): Likely in <p=55>Thessalonica</> (Tavern).
     +) Likes <trp=718>Lucius Modius minor</>
     -) Hates <trp=716>Ra Karak</>
     -) Hates <trp=722>Josephus</>
<trp=713>Anicius</> (Roman): Likely in <p=24>Massilia</> (Tavern).
     +) Likes <trp=714>Fabianus</>
     -) Hates <trp=725>Kara Boga</>
     -) Hates <trp=707>Libertus Tiro</>
<trp=714>Fabianus</> (Roman): Likely in <p=23>Augusta</> (Tavern).
     +) Likes <trp=715>Rombus</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=711>Albinus Basilius</>
<trp=715>Rombus</> (Roman): Likely in <p=28>Ancyra</> (Streets).
     +) Likes <trp=713>Anicius</>
     -) Hates <trp=701>Titocuna</>
     -) Hates <trp=704>Tertius Maior</>
<trp=716>Ra Karak</> (Berber): Joins during quest.
<trp=717>Gaius Lemonius</> (Roman): Likely in <p=54>Neapolis</> (Streets).
     +) Likes <trp=688>Pulchra</>
     -) Hates <trp=718>Lucius Modius minor</>
<trp=718>Lucius Modius minor</> (Roman): Likely in <p=53>Tarentum</> (Streets).
     -) Hates <trp=717>Gaius Lemonius</>
<trp=719>Ligia</> (Germanic): Likely in <p=26>Roma</> (Backstreets).
     +) Likes <trp=721>Marcus Vinicius</>
     -) Hates <trp=723>Elazar Bar Yochai</>
     -) Hates <trp=725>Kara Boga</>
<trp=720>Ursus</> (Germanic): Joins together with Ligia.
     -) Hates <trp=725>Kara Boga</>
<trp=721>Marcus Vinicius</> (Roman): Likely in <p=26>Roma</> (Tavern).
     +) Likes <trp=719>Ligia</>
     -) Hates <trp=723>Elazar Bar Yochai</>
<trp=722>Josephus</> (Judean): Likely in <p=116>Masada</> (Streets).
     +) Likes <trp=690>Satibarzanes</>
     -) Hates <trp=712>Lucullus Caepio</>
     -) Hates <trp=703>Arminius Octavianus</>
<trp=723>Elazar Bar Yochai</> (Judean): Likely in <p=49>Leptis Magna</> (Streets).
     +) Likes <trp=722>Josephus</>
     -) Hates <trp=721>Marcus Vinicius</>
     -) Hates <trp=719>Ligia</>
<trp=724>Mathildiz</> (Germanic): Joins during quest.
<trp=725>Kara Boga</> (Egyptian): Likely in <p=40>Alexandria</> (Tavern).
     +) Likes <trp=703>Arminius Octavianus</>
     -) Hates <trp=713>Anicius</>
     -) Hates <trp=719>Ligia</>
<trp=726>Eamane Turakina</> (Saka): Joins during quest.
<trp=727>Chaditox</> (Sarmatian): Likely in <p=46>Siracena</> (Streets).
     +) Likes <trp=705>Secundus Minor</>
     -) Hates <trp=709>Sidonius Apollinaris</>
"""

# Initialize Network
net = Network(height='900px', width='100%', bgcolor='#222222', font_color='white')

lines = data.strip().split('\n')

# --- PASS 1: Create Nodes ---
for line in lines:
    comp_match = re.search(r"<trp=\d+>(.*?)</> \((.*?)\): (.*)", line)

    if comp_match:
        name = comp_match.group(1)
        culture = comp_match.group(2)
        raw_location = comp_match.group(3)

        # Clean up location
        location = re.sub(r"<p=\d+>", "", raw_location).replace("</>", "")

        # Tooltip content
        tooltip_text = f"{name}\n------------------\nCulture: {culture}\nLocation: {location}"

        # Color Logic
        color = '#3b82f6'                            # Default: Medium Blue
        if 'Roman' in culture: color = '#8e44ad'     # Roman: Rich Purple
        elif 'Parthian' in culture: color = '#d35400' # Parthian: Burnt Orange
        elif 'Germanic' in culture or 'Britonic' in culture: color = '#27ae60' # Barbarian: Forest Green
        elif 'Egyptian' in culture: color = '#f1c40f' # Egyptian: Gold
        elif 'Judean' in culture: color = '#3498db'   # Judean: Dark Cyan
        elif 'Sarmatian' in culture: color = '#c0392b' # Sarmatian: Deep Red

        #draw the node (companion)
        net.add_node(
            name,
            label=name,
            title=tooltip_text,
            color=color,
            shape='box',
            borderWidth=1,
            # size=35,
            font={
                'size': 40,
                'color': 'white',
                'strokeWidth': 4,
                'strokeColor': 'black'
            }
        )

# --- PASS 2: Create Relationships ---
current_comp = None

for line in lines:
    comp_match = re.search(r"<trp=\d+>(.*?)</> \((.*?)\):", line)
    if comp_match:
        current_comp = comp_match.group(1)
        continue

    if current_comp:
        rel_match = re.search(r"([+\-])\)\s(Likes|Hates)\s<trp=\d+>(.*?)</>", line)
        if rel_match:
            sign = rel_match.group(1)
            target_name = rel_match.group(3)

            node_list = [n['id'] for n in net.nodes]
            if target_name not in node_list:
                continue

            if sign == '+':
                net.add_edge(current_comp, target_name, color='#66ff66', width=3, title="Likes")
            else:
                net.add_edge(current_comp, target_name, color='#ff6666', width=1, dashes=True, title="Hates")

# Settings
net.barnes_hut(gravity=-3000, central_gravity=0.3, spring_length=200, spring_strength=0.05, damping=0.09)
# net.show_buttons(filter_=['physics'])
net.show('website/content/companion_graph.html', notebook=False)