```python
import json
from pyvis.network import Network
from utils import SCRAPED_DATA_PATH

def load_data():
    with open(SCRAPED_DATA_PATH, 'r') as file:
        data = json.load(file)
    return data

def create_network_graph():
    data = load_data()
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    # add nodes
    for node in data['nodes']:
        net.add_node(node['id'], label=node['label'])

    # add edges
    for edge in data['edges']:
        net.add_edge(edge['from'], edge['to'])

    # save the graph
    net.show("network_graph.html")

if __name__ == "__main__":
    create_network_graph()
```